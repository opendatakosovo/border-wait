WAIT_TIME_GIF_URLS = {
   'great': [
      'http://i.giphy.com/kGMPV3ehtc7aE.gif',
      'http://i.giphy.com/UKm1AF0UrCkb6.gif',
      'http://i.giphy.com/qcMjXuCugvMXK.gif',
      'http://i.giphy.com/A854pmlcoiHni.gif',
      'http://i.giphy.com/cAfaWIcWr7qus.gif',
      'http://i.giphy.com/mIMsLsQTJzAn6.gif',
      'http://i.giphy.com/CAxbo8KC2A0y4.gif',
      'http://i.giphy.com/qCYJu1d0VfJTy.gif',
      'http://i.giphy.com/3otPoHqjMbo6JJ1FMk.gif',
      'http://i.giphy.com/UjSdO0uoyGeac.gif',
      'http://i.giphy.com/UiJ8YgFH2hlC.gif'
   ],
   'ok': [
      'http://i.giphy.com/3o7TKCGuEkIrLZ0E2Q.gif',
      'http://i.giphy.com/cPngiJPGKsfUQ.gif',
      'http://i.giphy.com/g790a3PzUHbs4.gif',
      'http://i.giphy.com/RIymi3HoG8jNS.gif',
      'http://i.giphy.com/QZbB48rGqylYk.gif',
      'http://i.giphy.com/xT0BKBY1YIfxxtk092.gif',
      'http://i.giphy.com/11fucLQCTOdvBS.gif',
      'http://i.giphy.com/pFkbkttdEBnSo.gif',
      'http://i.giphy.com/g0MQ2Pyi5Z3s4.gif',
      'http://i.giphy.com/9B5DEBbKQwwQE.gif'
   ]
   ,
   'bad': [
      'http://i.giphy.com/xTiTniwPRUeB59PNQc.gif',
      'http://i.giphy.com/bP2bOuWDpVM7C.gif',
      'http://i.giphy.com/NN5cAmTFRxpE4.gif',
      'http://i.giphy.com/rEKMO9OWtXjZS.gif',
      'http://i.giphy.com/3o6EhXIhX0HUX5nrsk.gif',
      'http://i.giphy.com/br7gVfL2SRdJK.gif',
   ],
   'horrible': [
      'http://i.giphy.com/59KddieNEF2GQ.gif',
      'http://i.giphy.com/3o7TKFdhXnKtxbn6wg.gif',
      'http://i.giphy.com/nAezPM5bCcuYw.gif',
      'http://i.giphy.com/3o7qE3a5YpLpCdeq0U.gif',
      'http://i.giphy.com/4n9lYreyEcn3a.gif',
      'http://i.giphy.com/4jCxItUVMfHig.gif',
      'http://i.giphy.com/nEL6rKDWEonGU.gif',
      'http://i.giphy.com/xT5LMFVIKfCsH0rkoo.gif',
      'http://i.giphy.com/l46CmHfsiZhKSERxe.gif',
      'http://i.giphy.com/REPi7Zrx4xf5S.gif'
   ]
}

for i in WAIT_TIME_GIF_URLS:
    for j in WAIT_TIME_GIF_URLS[i]:
        gif = j.split('/')[3]
        request = requests.get(j, stream=True)
        if request.status_code == 200:
            with open(gif, 'wb') as gf:
                for chunk in request:
                    gf.write(chunk)
