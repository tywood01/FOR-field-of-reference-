

const staticCacheName = `kam${new Date().getTime()}`;
const filesToCache = [
    '/kam/home',
    '/kam/',
    '/static/css/styles.css',
    '/static/templates/offline.html',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-30.png',
    '/static/images/appimages/windows11/StoreLogo.scale-150.png',
    '/static/images/appimages/windows11/Square150x150Logo.scale-125.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-40.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-48.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-72.png',
    '/static/images/appimages/windows11/Wide310x150Logo.scale-150.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-64.png',
    '/static/images/appimages/windows11/SmallTile.scale-150.png',
    '/static/images/appimages/windows11/Wide310x150Logo.scale-400.png',
    '/static/images/appimages/windows11/LargeTile.scale-150.png',
    '/static/images/appimages/windows11/LargeTile.scale-100.png',
    '/static/images/appimages/windows11/SplashScreen.scale-100.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-40.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-40.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-48.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-32.png',
    '/static/images/appimages/windows11/SplashScreen.scale-400.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-36.png',
    '/static/images/appimages/windows11/SmallTile.scale-125.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-24.png',
    '/static/images/appimages/windows11/Square44x44Logo.scale-150.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-44.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-16.png',
    '/static/images/appimages/windows11/SplashScreen.scale-125.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-20.png',
    '/static/images/appimages/windows11/LargeTile.scale-200.png',
    '/static/images/appimages/windows11/LargeTile.scale-400.png',
    '/static/images/appimages/windows11/SmallTile.scale-200.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-72.png',
    '/static/images/appimages/windows11/Square44x44Logo.scale-400.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-96.png',
    '/static/images/appimages/windows11/SmallTile.scale-400.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-48.png',
    '/static/images/appimages/windows11/SplashScreen.scale-150.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-30.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-24.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-256.png',
    '/static/images/appimages/windows11/Square150x150Logo.scale-200.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-64.png',
    '/static/images/appimages/windows11/SmallTile.scale-100.png',
    '/static/images/appimages/windows11/Square44x44Logo.scale-100.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-36.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-24.png',
    '/static/images/appimages/windows11/Wide310x150Logo.scale-200.png',
    '/static/images/appimages/windows11/Square150x150Logo.scale-150.png',
    '/static/images/appimages/windows11/Square44x44Logo.scale-125.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-60.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-256.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-96.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-60.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-80.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-16.png',
    '/static/images/appimages/windows11/Wide310x150Logo.scale-100.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-72.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-256.png',
    '/static/images/appimages/windows11/StoreLogo.scale-100.png',
    '/static/images/appimages/windows11/Wide310x150Logo.scale-125.png',
    '/static/images/appimages/windows11/Square150x150Logo.scale-400.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-32.png',
    '/static/images/appimages/windows11/LargeTile.scale-125.png',
    '/static/images/appimages/windows11/Square44x44Logo.scale-200.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-32.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-20.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-20.png',
    '/static/images/appimages/windows11/StoreLogo.scale-400.png',
    '/static/images/appimages/windows11/SplashScreen.scale-200.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-80.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-30.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-80.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-96.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-64.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-60.png',
    '/static/images/appimages/windows11/StoreLogo.scale-200.png',
    '/static/images/appimages/windows11/Square150x150Logo.scale-100.png',
    '/static/images/appimages/windows11/Square44x44Logo.targetsize-36.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-16.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-lightunplated_targetsize-44.png',
    '/static/images/appimages/windows11/StoreLogo.scale-125.png',
    '/static/images/appimages/windows11/Square44x44Logo.altform-unplated_targetsize-44.png',
    '/static/images/appimages/android/android-launchericon-512-512.png',
    '/static/images/appimages/android/android-launchericon-96-96.png',
    '/static/images/appimages/android/android-launchericon-72-72.png',
    '/static/images/appimages/android/android-launchericon-144-144.png',
    '/static/images/appimages/android/android-launchericon-48-48.png',
    '/static/images/appimages/android/android-launchericon-192-192.png',
    '/static/images/appimages/ios/192.png',
    '/static/images/appimages/ios/144.png',
    '/static/images/appimages/ios/80.png',
    '/static/images/appimages/ios/128.png',
    '/static/images/appimages/ios/16.png',
    '/static/images/appimages/ios/256.png',
    '/static/images/appimages/ios/58.png',
    '/static/images/appimages/ios/57.png',
    '/static/images/appimages/ios/60.png',
    '/static/images/appimages/ios/167.png',
    '/static/images/appimages/ios/100.png',
    '/static/images/appimages/ios/114.png',
    '/static/images/appimages/ios/1024.png',
    '/static/images/appimages/ios/72.png',
    '/static/images/appimages/ios/512.png',
    '/static/images/appimages/ios/32.png',
    '/static/images/appimages/ios/120.png',
    '/static/images/appimages/ios/40.png',
    '/static/images/appimages/ios/50.png',
    '/static/images/appimages/ios/29.png',
    '/static/images/appimages/ios/76.png',
    '/static/images/appimages/ios/180.png',
    '/static/images/appimages/ios/64.png',
    '/static/images/appimages/ios/87.png',
    '/static/images/appimages/ios/152.png',
    '/static/images/appimages/ios/20.png',
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("appname-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    console.log(event)
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                console.log(response)
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('offline');
            })
    )
});


self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', () => self.clients.claim());

