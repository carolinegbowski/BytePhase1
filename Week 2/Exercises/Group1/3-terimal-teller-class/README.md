## Terminal Teller Account Class

### Suggested Group-Work

You are going to rewrite your account model as a class.

The idea is you should be able to create an Account and save it like so.

```python
mike = Account(firstname="Mike", lastname="Bloom", pin="0123", balance=3.5)
mike.save()
```

Where .save() assigns a new random account number if the Account has never
been saved before, or updates the account with that number if it has.

You should be able to load a user with a class method of the Account class 
by either account number & pin or just account number 

```python
...
    mike = Account.login("012345678", "01234")
    if mike is not None:
        return mike
...
```

Complete the other methods as per the comments in `account.py`

Then rewrite your controller and views to use your class-based model instead
of the function-based one you wrote for the original project.

