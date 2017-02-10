# class Skilltree(object):
#     def view_studied(self):
#         for i in self:
#             print(i)





class Skilltree(object):
    def __init__(self):
        uin = input("How many topic are there?")
        read = int(uin)
        count = 0
        self.init_list = []
        rnumber = read
        while rnumber > count:
            rbook = input("please input topic {0}".format(count + 1))
            self.init_list.append(rbook)
            count += 1

        ui = input("Hello, How many topics Have you studied?")
        read = int(ui)
        count = 0
        self.rlist = []
        rnumber = read
        while rnumber > count:
            rbook = input("please input topic {0}".format(count + 1))
            self.rlist.append(rbook)
            count += 1





    # list = ['1','2','3','4','5','6','7']
    # for i in list:
    #     print()

    def notstudied(self):
        l1=self.init_list
        l2=self.rlist
        subjects=set(l1)-set(l2)
        return "this is/are the topic(s) you have not studied" + str(list(subjects))

    def studied(self):
        return "This are the topics studied" + str(self.rlist)




a=Skilltree()
print(a.studied())
print(a.notstudied())
