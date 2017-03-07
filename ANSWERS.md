1. To measure the performance of the service I would use a tool like
   `seige`, which is a linux command line tool for HTTP stress testing. Using the
   Gunicorn production server you could measure average response
   time as a function of the number of Gunicorn workers to find an optimal
   number for your machine. Too many workers creates alot of concurrency but,
   to much overhead for thread switching, too few could create timeouts for new connections.

2. To really scale this solution you would have to run a cluster of seperate
   machines behind a load balancing pool.
   If you needed to reduce the runtime of the individual threads, you could
   save time by increasing the granularity of the output ASCII. For performance
   with very large images, we could write the conversion kernel (image array
   scan) in C or C++ and call out to it using CFFI or Cython.

3. In the simplest form, saving images could be done locally on the server.
   To recreate the ASCII art for an previously uploaded image, we would need
   to modify our `/artify` endpoint to accept some type of file identifier,
   (a hash of the creation timestamp and a random number perhaps), which would
   be returned to the user on upload.

   Realisitically a service with any kind of state persistence would require
   user authentication and some kind of database. Each image file would get
   an ID, and a DB record belonging to the uploading user. The record would
   contain the image ID (and other metadata). This would allow a user to query
   all of their uploaded images. If we were using a distributed system and not a single
   instance we would need to store the images in a cloud service like AWS S3
   and then look up the image on whichever instance of our cluster was handling
   the request.


