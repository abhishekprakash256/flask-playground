from pymongo import MongoClient


#class for the database connection ini

client = MongoClient()


class Helper_fun():

    def make_database(self,db_name):
        """
        make the database
        """

        #make the database
        db = client["articles"]


    def make_collection(self,db_name,collection_name):
        """
        make the colcection in the database
        """

        #make the collection in the datbase

        pass





       





helper = Helper_fun()
helper.make_database("articles")
