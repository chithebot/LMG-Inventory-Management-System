import datetime

import entity
from ims_constants import *


class User(entity.Entity):
    """ This class represents a user.

        Attributes:
            _username (string)  : the user's username
            _password (string)  : the user's password
    """
    __doc__ += ('\n' + entity.Entity.__doc__)


    """
    This function initializes an User object.

    Args:
        self (User)		               : the current User object
        name (string)	               : the name of the User object
        username (string)	           : the username of the User object
        password (string)	           : the password of the User object
        security_question (int)        : the index of the security question associated with User
        security_question_ans (string) : the index of the security question answer associated with User
        last_login_attempt (datetime)  : the time of last login attempt
        login_attempts (int)           : number of times User account had attempted login
    """ 
    def __init__(self, name="", username="", password="", security_question=None,
                 security_question_ans=None, last_login_attempt=None, login_attempts=0):
        super().__init__(name)
        self._username = username
        self._password = password
        self._security_question = security_question
        self._security_question_ans = security_question_ans
        self._last_login_attempt = last_login_attempt
        self._login_attempts = login_attempts


    """
    This function gets the User object's username.

    Args:
        self (User) : the current User object
    
    Returns:
        Returns the User object's username.
    """ 
    @property
    def username(self):
        return self._username


    """
    This function gets the User object's username.

    Args:
        self (User) : the current User object
    
    Returns:
        Returns the User object's username.
    """ 
    @property
    def password(self):
        return self._password


    """
    This function gets the User object's security question number.

    Args:
        self (User) : the current User object
    
    Returns:
        Returns the User object's security question number.
    """ 
    @property
    def security_question(self):
        return self._security_question


    """
    This function gets the User object's security question answer.

    Args:
        self (User) : the current User object
    
    Returns:
        Returns the User object's security question answer.
    """ 
    @property
    def security_question_ans(self):
        return self._security_question_ans


    """
    This function gets the User object's last login attempt time.

    Args:
        self (User) : the current User object
    
    Returns:
        Returns the User object's last login attempt time.
    """ 
    @property
    def last_login_attempt(self):
        return self._last_login_attempt


    """
    This function gets the User object's login attempts.

    Args:
        self (User) : the current User object
    
    Returns:
        Returns the User object's login attempts.
    """ 
    @property
    def login_attempts(self):
        return self._login_attempts


    """
    This function gets the User object's account is locked and returns
    True if it is; False, otherwise. The account is considered locked if
    the login attempts is at the max number of attempts.


    Args:
        self (User) : the current User object
    
    Returns:
        Returns True if the account is locked; False, otherwise.
    """
    def isLocked(self):
        return self.login_attempts >= MAX_LOGIN_ATTEMPTS


    """
    This function checks if the User account is unlockable based
    on the last login attempt time and current time. If enough time
    has elapsed since the last login attempt time and current time,
    the account can be unlocked and True is returned; False, otherwise.

    Args:
        self (User) : the current User object
    
    Returns:
        Returns True if the account is unlockable; False, otherwise.
    """
    def isUnlockable(self):

        # Handles cases there is no login attempt yet or account is not locked
        if self.last_login_attempt is None or not self.isLocked():
            return False

        # Handles case where account is locked
        currentTime = datetime.datetime.now()
        deltaTime = currentTime - self.last_login_attempt
        minutesPassed = deltaTime.total_seconds() / 60
        return minutesPassed >= MINS_PASS_UNLOCK


    """
    This function gets the remaining time that the account is locked for.
    If the account is not locked, 0 is returned. The unit of time used is
    minutes. The minutes are rounded down

    Args:
        self (User) : the current User object
    
    Returns:
        Returns an float which represents the number of minutes the
        account is locked for.
    """
    def getRemainingLockDuration(self):

        # Handles case where account is not locked
        if not self.isLocked():
            return 0
        
        # Handles case where account is locked
        delta = datetime.datetime.now() - self.last_login_attempt
        minsPassed = delta.total_seconds() / 60
        minsRemaining = MINS_PASS_UNLOCK - minsPassed
        if minsRemaining <= 0:
            return 0
        return minsRemaining


    """
    This function sets the User object's username.

    Args:
        self (User)		  : the current User object
        username (string) : the new username to set
    """ 
    @username.setter
    def username(self, username):
        self._username = username


    """
    This function sets the User object's password.

    Args:
        self (User)		  : the current User object
        password (string) : the new password to set
    """ 
    @password.setter
    def password(self, password):
        self._password = password


    """
    This function sets the User object's security question number.

    Args:
        self (User)		        : the current User object
        security_question (int)	: the new security question to set
    """ 
    @security_question.setter
    def security_question(self, security_question):
        self._security_question = security_question


    """
    This function sets the User object's security question answer.

    Args:
        self (User)		                : the current User object
        security_question_ans (string)	: the new security answer to set
    """ 
    @security_question_ans.setter
    def security_question_ans(self, security_question_ans):
        self._security_question_ans = security_question_ans


    """
    This function sets the User object's last login attempt time.

    Args:
        self (User)		              : the current User object
        last_login_attempt (datetime) : the new last login attempt time to set
    """ 
    @last_login_attempt.setter
    def last_login_attempt(self, last_login_attempt):
        self._last_login_attempt = last_login_attempt


    """
    This function sets the User object's number of login attempts.

    Args:
        self (User)		     : the current User object
        login_attempts (int) : the new last login attempts to set
    """
    @login_attempts.setter
    def login_attempts(self, login_attempts):
        self._login_attempts = login_attempts


    """
    This function unlocks the User object's.

    Args:
        self (User) : the current User object
    """
    def unlock(self):
        self.login_attempts = 0


    """
    This function sets all of the current User object's
    attributes to empty strings, or clears them.

    Args:
        self (User)		    : the current User object
    """ 
    def clear(self):
        self.name = ""
        self.username = ""
        self.password = "" 
        self.security_question = None
        self.security_question_ans = None
        self.last_login_attempt = None
        self.login_attempts = 0


    """
    This function returns the string representation of the current
    User object.

    Args:
        self (User)	: the current User object

    Returns:
        Returns a string which represents the current User object.
    """
    def __str__(self):
        return super().__str__() + "\t" + self.username