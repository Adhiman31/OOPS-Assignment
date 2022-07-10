import logging
logging.basicConfig(filename="fsds.log",level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")

class string :

    def __init__(self,str):
        logging.info("This is string class constructor....")
        self.str = str

    def extract_String_In_Range(self):
        try :
            logging.info("This functiom extracts the string in range from given data set...")
            return self.str[0:300:3]
        except Exception as e :
            logging.error(e)

    def rev_string(self):
        try:
            logging.info("this function reverse the string from given data set...")
            return self.str[::-1]
        except Exception as e :
            logging.error(e)

    def split_str_after_uppperCase(self):
        try:
            logging.info("this function converts the given string data set into upper case and then spilts it....")
            return self.str.upper().split(' ')
        except Exception as e :
            logging.error(e)

    def convert_lower_str(self):
        try:
            logging.info("this function converts the given string data set to lower alphabets...")
            return self.str.capitalize()
        except Exception as e :
            logging.error(e)

    def str_is_AlphaNum(self ,s):
        try :
            logging.info("Checking if string is alpha numeric or not...")
            return s.isalnum()
        except Exception as e :
            logging.error(e)

    def str_is_Alpha(self ,s):
        try:
            logging.info("checking if string contains alphabets or not...")
            return s.isalpha()
        except Exception as e :
            logging.error(e)

    def str_expand_tabs(self,s):
        try:
            logging.info("this function expand the tabs for given data set")
            return s.expandtabs()
        except Exception as e :
            logging.error(e)

    def str_trim(self,s):
        try:
            logging.info("this function trims or removes the spaces from both sides of the string...")
            return s.strip()
        except Exception as e:
            logging.error(e)

    def left_strip(self,s):
        try:
            logging.info("removes the spaces from left of string")
            return s.lstrip()
        except Exception as e:
            logging.error(e)

    def right_strip(self,s):
        try:
            logging.info("removes spaces from right of string")
            return s.rstrip()
        except Exception as e:
            logging.error(e)

    def replace_char_str(self,word ,s1,s2):
        try:
            logging.info("replace character within a string")
            return word.replace(s1 ,s2)
        except Exception as e:
            logging.error(e)

    def center_align_str(self,s):
        try:
            logging.info("center aligns the string , using the specified character")
            return s.center(20,'a')
        except Exception as e:
            logging.error(e)

class list_Prac :

    def __init__(self,lst,lst2):
        logging.info("this is the constructor for list class")
        self.lst = lst
        self.lst2 = lst2

    def extract_list_entity(self):
        try:
            logging.info("extrating list entities from given data set...")
            for i in self.lst:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def extract_odd_val(self):
        try:
            logging.info("extracting all the odd values from list data set...")
            l1 = []
            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            for k in l1:
                if k % 2 != 0:
                    logging.info(k)
        except Exception as e:
            logging.error(e)

    def extract_word_inueron(self):
        try:
            logging.info("extracting word inueron from data set...")
            l2 = []
            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                            l2.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if g == 'ineuron':
                                l2.append(g)
            logging.info(l2)
        except Exception as e:
            logging.error(e)

    def unwrap_list(self):
        try:
            logging.info("unwrapping all the data in form of single list")
            l3 = []
            for i in self.lst:
                if type(i) == list or type(i) == dict or type(i) == set or type(i) == tuple:
                    for j in i:
                        l3.append(j)
            logging.info(l3)
        except Exception as e:
            logging.error(e)

    def extarct_spec_number(self):
        try:
            logging.info("extaract integer 456 from list ...")
            return self.lst2[5][1]
        except Exception as e:
            logging.error(e)


class dict_Prac :

    def __init__(self,lst):
        logging.info("constructor for dictionary class...")
        self.lst = lst


    def extract_dict_elements(self):
        try:
            logging.info("extracting all dictionary elements from data set")
            for i in self.lst:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def mumber_of_keys(self):
        try:
            logging.info("extracting number of keys in the dictionary in given data set")
            for i in self.lst:
                if type(i) == dict:
                    #logging.info("number of keys in  dict : ", len(i.keys()))
                     return len(i.keys())
        except Exception as e:
            logging.error(e)



class collection :

    def __init__(self,lst):
        logging.info("constructor for collection class")
        self.lst = lst

    def occurence_of_data(self):
        try:
            logging.info("finding out number of occurence of each data with the data set")
            l8 = []
            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l8.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                l8.append(g)

            for m in set(l8):
                logging.info('{0}:{1}'.format(m, l8.count(m)))
        except Exception as e:
            logging.error(e)



    def find_mul_of_allData(self):
        try:
            logging.info("finding out multiplication of all individual data")
            for i in self.lst:
                m = 1
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            m = m * j

                if type(i) == dict:
                    for k in i.items():
                        for n in k:
                            if type(n) == int:
                                m = m * n
                    return m
        except Exception as e:
            logging.error(e)


# creating objects of classes and calling functions


str_obj = string("this is My First Python programming class and i am learNING python string and its function")

logging.info("*********Creating object for String Class************")

logging.info(str_obj.extract_String_In_Range())

logging.info(str_obj.convert_lower_str())

logging.info(str_obj.rev_string())

logging.info(str_obj.split_str_after_uppperCase())

logging.info(str_obj.str_trim(' anil '))

logging.info(str_obj.left_strip('  anil'))

logging.info(str_obj.right_strip('anil  '))

logging.info(str_obj.center_align_str('dhiman'))

logging.info(str_obj.str_expand_tabs("anil\tkumar\tdhiman"))

logging.info(str_obj.replace_char_str('anil','n','k'))

logging.info(str_obj.str_is_Alpha('askftot'))

logging.info(str_obj.str_is_AlphaNum('abc124'))

logging.info("***************end of string class functions*********************")

lst_obj = list_Prac([[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1': "sudh" ,"k2": "ineuron",'k3':"kumar" ,3 :6,7:8},["ineuron" ,"data science"]],
                    [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])

logging.info("*****list_Prac class object created*******")

logging.info(lst_obj.unwrap_list())

logging.info(lst_obj.extract_list_entity())

logging.info(lst_obj.extract_odd_val())

logging.info(lst_obj.extarct_spec_number())

logging.info(lst_obj.extract_word_inueron())


logging.info("*************************end of list_Prac class*********************")

dict_obj = dict_Prac([[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1': "sudh" ,"k2": "ineuron",'k3':"kumar" ,3 :6,7:8},["ineuron" ,"data science"]])

logging.info("****************************Object for Dict_Pract class created*******************************")

logging.info(dict_obj.extract_dict_elements())

logging.info(dict_obj.mumber_of_keys())

logging.info("*****************************end of Dict_Prac class*************************")

coll_obj = collection([[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1': "sudh" ,"k2": "ineuron",'k3':"kumar" ,3 :6,7:8},["ineuron" ,"data science"]])

logging.info("*****************Object for collection class created***********************")

logging.info(coll_obj.find_mul_of_allData())

logging.info(coll_obj.occurence_of_data())

logging.info("*******************************end of collection class***********************************")




























