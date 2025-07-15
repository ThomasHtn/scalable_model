PYTHONPATH=.
	
populate-db:
	PYTHONPATH=$(PYTHONPATH) python3 database/modules/populate_db.py