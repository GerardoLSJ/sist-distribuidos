public class LockManager {
 private Hashtable theLocks;
 public void setLock(Object object, TransID trans, LockType lockType) {
  Lock foundLock;
  synchronized(this) {
   // find the lock associated with object
   // if there isn’t one, create it and add it to the hashtable
  }
  foundLock.acquire(trans, lockType);
 }
 // synchronize this one because we want to remove all entries
 public synchronized void unLock(TransID trans) {
  Enumeration e = theLocks.elements();
  while (e.hasMoreElements()) {
   Lock aLock = (Lock)(e.nextElement());
   if ( /* trans is a holder of this lock*/ ) aLock.release(trans);
  }
 }
}