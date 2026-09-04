// Radar Esportes — permite abrir o site mesmo sem internet.
// Guarda a última versão da página; o conteúdo continua vindo ao vivo.

var CACHE = "radar-v1";
var ESSENCIAIS = ["./", "./index.html", "./manifest.json",
  "./icone-192.png", "./icone-512.png", "./icone-mask.png"];

self.addEventListener("install", function (evento) {
  self.skipWaiting();
  evento.waitUntil(
    caches.open(CACHE).then(function (c) {
      return c.addAll(ESSENCIAIS).catch(function () { return null; });
    })
  );
});

self.addEventListener("activate", function (evento) {
  evento.waitUntil(
    caches.keys().then(function (nomes) {
      return Promise.all(nomes.map(function (n) {
        if (n !== CACHE) { return caches.delete(n); }
        return null;
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener("fetch", function (evento) {
  var pedido = evento.request;
  if (pedido.method !== "GET") { return; }

  var url = new URL(pedido.url);
  var daCasa = url.origin === self.location.origin;

  // Notícias, placares e tabelas: sempre da internet, nunca do cache.
  if (!daCasa || url.pathname.indexOf("noticias.json") >= 0) { return; }

  // A página em si: tenta a internet e, se falhar, usa a guardada.
  evento.respondWith(
    fetch(pedido).then(function (resposta) {
      var copia = resposta.clone();
      caches.open(CACHE).then(function (c) { c.put(pedido, copia); });
      return resposta;
    }).catch(function () {
      return caches.match(pedido).then(function (guardada) {
        return guardada || caches.match("./index.html");
      });
    })
  );
});
