python-firebase-gae
======
python-firebase-gae is a python wrapper for Firebase's REST API that was produced specifically to run in the Google App Engine enviroment (doesn't use the `requests` library). It uses `urlfetch`.

Some alternatives include

* [Python Firebase](https://github.com/ozgur/python-firebase)
* [Python Firebase by Michael Huynh](https://github.com/mikexstudios/python-firebase)

Both of which use the `requests` library.

Using
======

Clone it into the `/lib/firebase` folder:

    $ git clone http://github.com/benletchford/python-firebase-gae lib/firebase

Import it:

    from lib.firebase.wrapper import Firebase

Instantiate it:

    ref = Firebase('https://example.firebaseio.com/users')

Or with authentication:

    ref = Firebase('https://example.firebaseio.com/users', 'auth-token')
