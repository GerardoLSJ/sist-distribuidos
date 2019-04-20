public class Lock {
	private Object object;  	// the object being protected by the lock
	private Vector holders;		// the TIDs of current holders
	private LockType lockType; 	// the current type

	public synchronized void acquire(TransID trans, LockType aLockType ){
		while(/*another transaction holds the lock in conflicting mode*/) {
			try {
				wait();
			}catch ( InterruptedException e){/*...*/ }
		}

		if (holders.isEmpty()) { // no TIDs hold lock
			holders.addElement(trans);
			lockType = aLockType;
		}
		else if (/*another transaction holds the lock, share it*/ ) {
			if (/* this transaction not a holder*/) 
				holders.addElement(trans);
		} else if (/* this transaction is a holder but needs a more exclusive lock*/) {
			lockType.promote();
		}
	}
	
	public synchronized void release(TransID trans ){
		holders.removeElement(trans); // remove this holder
		// set locktype to none
		notifyAll();
	}
}