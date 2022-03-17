from tkinter import *
import tkinter.messagebox
from tkinter.messagebox import askyesno
from treelib import Node, Tree
import re

tab = re.compile('\t+')
whitespace = re.compile('\s+')
keyword = re.compile(r'\bint\b|\bfloat\b|\belse\b|\bif\b')
any_integer = re.compile('^\d+') #'^\d+$' can also be used
Float_literal = re.compile('\d+\.\d+')
identifiers = re.compile('[A-z]+\d+|[A-z]+')
operator = re.compile('[+]|[=]|[>]|[*]')
separator = re.compile('[(]|[)]|[:]|["]|[;]|[“]|[”]')
str = re.compile('"(.+?)"|“(.+?)”') #"(.+?)"|“(.+?)”

class msgData:
    def __init__(self):
        self.msg = ""
        self.cnt = 0
    def add_msg(self,msg):
        self.msg = msg
    def print_msg(self):
        print(self.msg)
    def split(self,chr):
        self.msg=self.msg.split(chr)
    def size(self):
        count = 0
        for item in self.msg:
            count+=1
        return count
    def get_el(self,i):
        return self.msg[i]
    def evaluate(self):
        for i in range(len(self.msg)):
            if self.msg[i] != "":
                return True
        return False
    def get_tree(self):
        return self.tree
    def remove_whitespace(self,str):
        if whitespace.match(str) != None:
            result = whitespace.match(str)
            newRes = str.replace(str[result.start():result.end()], "", 1)
            return newRes
        else:
            return str

    # print(remove_whitespace('int    A1=5'))

    def lexer(self,string):
        resList = []
        while string != "":

            string = self.remove_whitespace(string)  # I could use strip() here
            # print(string)

            if str.match(string) != None:
                result = str.match(string)
                str1 = result.group(0)
                resList.append("sep, {}".format(str1[result.start()]))
                resList.append("str_lit, {}".format(str1[result.start() + 1:result.end() - 1]))
                resList.append("sep, {}".format(str1[result.end() - 1]))
                string = string.replace(string[result.start():result.end()], "", 1)
                string = self.remove_whitespace(string)
                # print(string)
            if keyword.match(string) != None:
                result = keyword.match(string)
                resList.append("key, {}".format(result.group(0)))
                string = string.replace(string[result.start():result.end()], "", 1)
                string = self.remove_whitespace(string)
                # print(string)

            if separator.match(string) != None:
                result = separator.match(string)
                resList.append("sep, {}".format(result.group(0)))
                # print(result.group(0))
                string = string.replace(string[result.start():result.end()], "", 1)
                string = self.remove_whitespace(string)
                continue
                # print(string)

            if identifiers.match(string) != None:
                result = identifiers.match(string)
                resList.append("id, {}".format(result.group(0)))
                string = string.replace(string[result.start():result.end()], "", 1)
                string = self.remove_whitespace(string)
                # print(string)

            if operator.match(string) != None:
                result = operator.match(string)
                resList.append("op, {}".format(result.group(0)))
                string = string.replace(string[result.start():result.end()], "", 1)
                string = self.remove_whitespace(string)
                # print(string)

            if Float_literal.match(string) != None:
                result = Float_literal.match(string)
                resList.append("fl_lit, {}".format(result.group(0)))
                string = string.replace(string[result.start():result.end()], "", 1)
                string = self.remove_whitespace(string)
                # print(string)

            if any_integer.match(string) != None:
                result = any_integer.match(string)
                resList.append("int_lit, {}".format(result.group(0)))
                string = string.replace(string[result.start():result.end()], "", 1)
                string = self.remove_whitespace(string)
                # print(string)
            """else:
                print("lexer failed...")
                return 0"""

        self.output = ""
        for i in range(len(resList)):
            self.output += "{}\n".format(resList[i])

        return self.output


    def parse(self):
        self.tree = Tree()

        self.parseOP = ""
        parseList = self.output.split("\n")
        print(parseList)

        self.tokens = []
        for i in range(len(parseList)):
            self.tokens.append(tuple(parseList[i].split(", ")))

        print(self.tokens)

        self.inToken = ("empty", "empty")

        global inToken
        inToken = self.tokens.pop(0)
        if inToken[1] == "float":
            self.exp()
        elif inToken[1] == "if":
            self.if_exp()
        elif inToken[1] == "print":
            self.print_exp()
        else:
            print("No parsing method declared")
            self.parseOP += "No parsing method declared"

        self.tree.show()
        self.tree.save2file("tree.txt",reverse=True)

        return self.parseOP




    def accept_token(self):
        global inToken
        print("     accept token from the list:" + inToken[1])
        self.parseOP += "\n     accept token from the list: {}\n".format(inToken[1])
        inToken = self.tokens.pop(0)

    def math(self):
        self.multi()
        if (inToken[1] == "+"):
            print("child node (token):" + inToken[1])
            self.tree.create_node("+", "+", parent="math")  # tree
            self.parseOP += "\nchild node (token): {}\n".format(inToken[1])
            self.accept_token()

        self.multi()

    def multi(self):
        self.cnt +=1
        print("\n----parent node math, finding children nodes:")
        self.parseOP += "\n----parent node math, finding children nodes:\n"
        self.tree.create_node("multi", "multi{}".format(self.cnt), parent="math")  # tree


        global inToken
        if (inToken[0] == "fl_lit"):
            print("child node (internal): float")
            self.tree.create_node("fl_lit", "fl_{}".format(self.cnt), parent="multi{}".format(self.cnt))  # tree
            self.tree.create_node(inToken[1], "float_val_multi{}".format(self.cnt), parent="fl_{}".format(self.cnt))  # tree
            self.parseOP += "\nchild node (internal): float\n"
            print("   float has child node (token):" + inToken[1])
            self.parseOP += "\n   float has child node (token):{}\n".format(inToken[1])
            self.accept_token()


        elif (inToken[0] == "int_lit"):
            print("child node (internal): int")
            self.tree.create_node("int", "int_multi", parent="multi{}".format(self.cnt))  # tree
            self.tree.create_node(inToken[1], "int_val_multi", parent="int_multi")  # tree"""
            self.parseOP += "\nchild node (internal): int\n"
            print("   int has child node (token):" + inToken[1])
            self.parseOP += "\n   int has child node (token):{}\n".format(inToken[1])

            self.accept_token()

            if (inToken[1] == "*"):
                print("child node (token):" + inToken[1])
                self.parseOP += "\nchild node (token):{}\n".format(inToken[1])
                self.accept_token()
                self.tree.create_node("*","*",parent="multi{}".format(self.cnt)) #tree

                print("child node (internal): multi")
                self.parseOP += "\nchild node (internal): multi\n"
                self.multi()
            else:
                print("error, you need + after the int in the math")
                self.parseOP += "\nerror, you need + after the int in the math\n"

        else:
            print("error, math expects float or int")
            self.parseOP += "\nerror, math expects float or int\n"

    def exp(self):
        self.tree.create_node("exp", "exp")  # tree
        print("\n----parent node exp, finding children nodes:")
        self.parseOP += "\n----parent node exp, finding children nodes:\n"
        global inToken
        typeT, token = inToken
        if (typeT == "key"):
            self.tree.create_node("keyword", "keyword",parent="exp")  # tree
            print("child node (internal): keyword")
            self.parseOP += "\nchild node (internal): keyword\n"
            print("   identifier has child node (token):" + token)
            self.tree.create_node(token, "key", parent="keyword")  # tree
            self.parseOP += "\n   identifier has child node (token):{}\n".format(token)
            self.accept_token()
            typeT, token = inToken
        else:
            # print(typeT)
            print("expect keyword as the first element of the expression!\n")
            self.parseOP += "\nexpect keyword <float / int> as the first element of the expression!\n"
            return
        if (typeT == "id"):
            print("child node (internal): identifier")
            self.tree.create_node("identifier", "identifier", parent="exp")  # tree
            self.tree.create_node(token, "id", parent="identifier")  # tree
            self.parseOP += "\nchild node (internal): identifier\n"
            print("   identifier has child node (token):" + token)
            self.parseOP += "\n   identifier has child node (token):\n"
            self.accept_token()
        else:
            print()
            self.parseOP += "\n\n"
            print("expect identifier as the first element of the expression!\n")
            self.parseOP += "\nexpect identifier as the first element of the expression!\n"

            return

        if (inToken[1] == "="):
            print("child node (token):" + inToken[1])
            self.tree.create_node("=", "op", parent="exp")  # tree
            self.parseOP += "\nchild node (token):{}\n".format(inToken[1])
            self.accept_token()
        else:
            print("expect = as the second element of the expression!")
            self.parseOP += "\nexpect = as the second element of the expression!\n"
            #print(inToken)
            return

        print("Child node (internal): math")
        self.tree.create_node("math", "math", parent="exp")
        self.parseOP += "\nChild node (internal): math\n"
        self.math()
        if (inToken[1] == ";"):
            print("child node (token):" + inToken[1])
            self.parseOP += "\nchild node (token):{}\n".format(inToken[1])
            # self.accept_token()
            print("success")
            self.parseOP += "\nsuccess\n"
        else:
            print("expect ; as the last element of the expression!")
            self.parseOP += "\nexpect ; as the last element of the expression!\n"
            # print(inToken)
            return

    def if_exp(self):
        print("\n----parent node exp, finding children nodes:")
        self.parseOP += "\n----parent node if_exp, finding children nodes:\n"
        self.tree.create_node("if_exp","if_exp")
        global inToken
        typeT, token = inToken
        if (token == "if"):
            print("child node (internal): keyword")
            self.parseOP += "\nchild node (internal): keyword\n"
            print("   identifier has child node (token):" + token)
            self.parseOP += "\n   identifier has child node (token):{}\n".format(token)
            self.tree.create_node("if","if",parent="if_exp")
            self.accept_token()
            typeT, token = inToken
        else:
            # print(typeT)
            print("expect keyword <if> as the first element of the expression!\n")
            self.parseOP += "\nexpect keyword as the first element of the expression!\n"
            return
        if (token == "("):
            print("child node (internal): separator")
            self.parseOP += "\nchild node (internal): separator\n"
            print("   separator has child node (token):" + token)
            self.parseOP += "\n   separator has child node (token):\n"
            self.tree.create_node("(","(",parent="if_exp")
            self.accept_token()
        else:
            print()
            self.parseOP += "\n\n"
            print("expect ( as the second element of the expression!\n")
            self.parseOP += "\nexpect identifier as the first element of the expression!\n"
            return

        print("Child node (internal): comparison_exp")
        self.parseOP += "\nChild node (internal): comparison_exp\n"
        self.comparison_exp()


        if (inToken[1] == ")"):
            print("child node (token):" + inToken[1])
            self.parseOP += "\nchild node (token):{}\n".format(inToken[1])
            self.tree.create_node(")", ")", parent="if_exp")
            self.accept_token()
        else:
            print("expect ) as the third element of the expression!")
            self.parseOP += "\nexpect ) as the third element of the expression!\n"
            #print(inToken)
            return

        if (inToken[1] == ":"):
            print("child node (token):" + inToken[1])
            self.parseOP += "\nchild node (token):{}\n".format(inToken[1])
            self.tree.create_node(":", ":", parent="if_exp")
            #self.accept_token()
            print("success")
            self.parseOP += "\nsuccess\n"
        else:
            print("expect : as the last element of the expression!")
            self.parseOP += "\nexpect : as the last element of the expression!\n"
            #print(inToken)
            return

    def comparison_exp(self):
        print("\n----parent node comparison_exp, finding children nodes:")
        self.parseOP += "\n----parent node comparison_exp, finding children nodes:\n"
        self.tree.create_node("comparison_exp", "comparison_exp", parent="if_exp")
        global inToken
        if (inToken[0] == "id"):
            print("child node (internal): id")
            self.parseOP += "\nchild node (internal): id\n"
            self.tree.create_node("identifier", "id1", parent="comparison_exp")
            print("   id has child node (token):" + inToken[1])
            self.parseOP += "\n   id has child node (token):{}\n".format(inToken[1])
            self.tree.create_node(inToken[1],"id1_child",parent="id1")
            self.accept_token()
        else:
            print("error, comparison_exp expects identifier")
            self.parseOP += "\nerror, comparison_exp expects identifier\n"
            return

        if (inToken[1] == ">") or (inToken[1] == "<") or (inToken[1] == ">=") or (inToken[1] == "<=") or (inToken[1] == "==") or (inToken[1] == "=!") :
            print("child node (internal): comparator")
            self.parseOP += "\nchild node (internal): comparator\n"
            print("  comparator has child node (token):" + inToken[1])
            self.parseOP += "\n   comparator has child node (token):{}\n".format(inToken[1])
            self.tree.create_node(inToken[1], "sep", parent="comparison_exp")
            self.accept_token()
        else:
            print("error, comparison_exp expects comparator")
            self.parseOP += "\nerror, comparison_exp expects comparator\n"
            return

        if (inToken[0] == "id"):
            print("child node (internal): id")
            self.parseOP += "\nchild node (internal): id\n"
            self.tree.create_node("identifier", "id2", parent="comparison_exp")
            print("   id has child node (token):" + inToken[1])
            self.parseOP += "\n   id has child node (token):{}\n".format(inToken[1])
            self.tree.create_node(inToken[1], "id2_child", parent="id2")
            self.accept_token()
        else:
            print("error, comparison_exp expects identifier")
            self.parseOP += "\nerror, comparison_exp expects identifier\n"
            return

    def print_exp(self):
        print("\n----parent node print_exp, finding children nodes:")
        self.parseOP += "\n----parent node print_exp, finding children nodes:\n"
        self.tree.create_node("print_exp","print_exp")
        global inToken
        typeT, token = inToken
        if (token == "print"):
            print("child node (internal): identifier")
            self.parseOP += "\nchild node (internal): identifier\n"
            print("   identifier has child node (token):" + token)
            self.parseOP += "\n   identifier has child node (token):{}\n".format(token)
            self.tree.create_node("print", "print",parent="print_exp")
            self.accept_token()
            typeT, token = inToken
        else:
            # print(typeT)
            print("expect identifier <print> as the first element of the expression!\n")
            self.parseOP += "\nexpect keyword as the first element of the expression!\n"
            return
        if (token == "("):
            print("child node (internal): separator")
            self.parseOP += "\nchild node (internal): separator\n"
            print("   separator has child node (token):" + token)
            self.parseOP += "\n   separator has child node (token):\n"
            self.tree.create_node("(", "(", parent="print_exp")
            self.accept_token()
            typeT, token = inToken
        else:
            print()
            self.parseOP += "\n\n"
            print("expect ( as the second element of the expression!\n")
            self.parseOP += "\nexpect identifier as the second element of the expression!\n"
            return

        if (token == '"') or token == '“':
            print("child node (internal): separator")
            self.parseOP += "\nchild node (internal): separator\n"
            print("   separator has child node (token):" + token)
            self.parseOP += "\n   separator has child node (token):\n"
            self.tree.create_node('"', "open_quote", parent="print_exp")
            self.accept_token()
            typeT, token = inToken
        else:
            print()
            self.parseOP += "\n\n"
            print(inToken)
            print("""expect " as the third element of the expression!\n""")
            self.parseOP += "\nexpect identifier as the third element of the expression!\n"
            return

        if (typeT == "str_lit"):
            print("child node (internal): str_lit")
            self.parseOP += "\nchild node (internal): str_lit\n"
            self.tree.create_node('string', "string", parent="print_exp")
            print("   str_lit has child node (token):" + token)
            self.parseOP += "\n   str_lit has child node (token):\n"
            self.tree.create_node(token, "string_lit", parent="string")
            self.accept_token()
            typeT, token = inToken
        else:
            print()
            self.parseOP += "\n\n"
            print(inToken)
            print("""expect " as the fourth element of the expression!\n""")
            self.parseOP += "\nexpect identifier as the fourth element of the expression!\n"
            return

        if (token == '"') or token == '”':
            print("child node (internal): separator")
            self.parseOP += "\nchild node (internal): separator\n"
            print("   separator has child node (token):" + token)
            self.parseOP += "\n   separator has child node (token):\n"
            self.tree.create_node('"', "close_quote", parent="print_exp")
            self.accept_token()
            typeT, token = inToken
        else:
            print()
            self.parseOP += "\n\n"
            print("""expect " as the fifth element of the expression!\n""")
            self.parseOP += "\nexpect identifier as the fifth element of the expression!\n"
            return

        if (token == ")"):
            print("child node (internal): separator")
            self.parseOP += "\nchild node (internal): separator\n"
            print("   separator has child node (token):" + token)
            self.parseOP += "\n   separator has child node (token):\n"
            self.tree.create_node(')', ")", parent="print_exp")
            self.accept_token()
            typeT, token = inToken
        else:
            print()
            self.parseOP += "\n\n"
            print("expect ) as the 7th element of the expression!\n")
            self.parseOP += "\nexpect identifier as the 7th element of the expression!\n"
            return
        if (inToken[1] == ";"):
            print("child node (token):" + inToken[1])
            self.parseOP += "\nchild node (token):{}\n".format(inToken[1])
            #self.accept_token()
            self.tree.create_node(';', ";", parent="print_exp")
            print("success")
            self.parseOP += "\nsuccess\n"
        else:
            print("expect ; as the last element of the expression!")
            self.parseOP += "\nexpect ; as the last element of the expression!\n"
            #print(inToken)
            return

    def parse_tree(self):
        f = open("tree.txt", "r", encoding="utf-8")
        self.s = ""
        for line in f:
            self.s += line
        f.close()

        return self.s
    def clear_file(self):
        file = open("tree.txt", "r+")
        file.truncate(0)
        file.close()




class lexer_GUI:

    def __init__(self,root):
        self.master = root
        self.master.title("Lexical Analyzer for TinyPie")

        self.frame = Frame(self.master,background="blue",height=50)

        ################----------START OF SOURCE CODE INPUT TEXT BOX-----------###########################
        self.label = Label(self.master, text="Source Code Input",font="Courier",pady=20)
        self.label.grid(row=0, column=1)

        self.t = Text(self.master, width=60, height=20)
        self.t.grid(column=1, row=1,sticky=NSEW,rowspan=4,padx=(0,20))
        root.grid_columnconfigure(1, weight=1)
        ################----------END OF SOURCE CODE INPUT TEXT BOX-----------###########################

        ################----------START OF LEXICAL ANALYZED OUTPUT TEXT BOX-----------###########################
        self.label = Label(self.master, text="Lexical Analyzed Result",font="Courier")
        self.label.grid(row=0, column=2)

        self.w = Text(self.master, width=30, height=10, fg="green", font="Courier",highlightcolor="green",highlightbackground="green",highlightthickness=5,bg="black")
        self.w.grid(column=2, row=1,sticky=NSEW,rowspan=4,padx=(0,20))
        #root.grid_columnconfigure(2, weight=1)
        ################----------END OF LEXICAL ANALYZED OUTPUT TEXT BOX-----------###########################

        ################----------START OF PARSED OUTPUT TEXT BOX-----------###########################
        self.label = Label(self.master, text="Parse Output", font="Courier")
        self.label.grid(row=6, column=1)

        self.p = Text(self.master, width=60, height=20)
        self.p.grid(column=1, row=7, sticky=NSEW,padx=(0,20))
        #root.grid_columnconfigure(2, weight=1)
        ################----------START OF PARSED OUTPUT TEXT BOX-----------###########################

        ################----------START OF PARSE TREE OUTPUT TEXT BOX-----------###########################
        self.label = Label(self.master, text="Parse Tree Output", font="Courier")
        self.label.grid(row=6, column=2)

        self.q = Text(self.master, width=30, height=10)
        self.q.grid(column=2, row=7, sticky=NSEW, rowspan=4,padx=(0,20))
        # root.grid_columnconfigure(2, weight=1)
        ################----------END OF PARSE TREE OUTPUT TEXT BOX-----------###########################

        ################----------START OF CURRENT PROCESSING OUTPUT TEXT BOX-----------###########################
        self.label = Label(self.master, text="Current Processing Line:", pady=0, padx=50)
        self.label.grid(row=4, column=0, sticky=W)

        self.entry = Entry(self.master)
        self.entry.configure(width=5,justify=CENTER,state=DISABLED)
        self.entry.grid(row=5, column=0)
        ################----------END OF CURRENT PROCESSING OUTPUT TEXT BOX-----------###########################



        ################----------BUTTONS-----------###########################

        self.quit_button = Button(self.master, text="Quit", command=self.confirm, height=2, width=10, background="red",font="Courier")
        self.quit_button.grid(row=3, column=0,padx=2,pady=2)

        self.next_button = Button(self.master,text="Next Line",command=self.next,height=2,width=10,background="green",font="Courier")
        self.next_button.grid(row=1,column=0,padx=2,pady=2)

        self.reset_button = Button(self.master, text="Reset", command=self.reset, height=2, width=10,background="orange", font="Courier")
        self.reset_button.grid(row=2, column=0,padx=2,pady=2)

        ################----------BUTTONS-----------###########################

        self.data = msgData()
        self.counter = 0
        self.s = ""
        self.parse_op = ""
    def reset(self):
        self.counter = 0
        self.t.configure(state=NORMAL)
        self.t.delete(0.0,END)
        self.w.configure(state=NORMAL)
        self.w.delete(0.0,END)
        self.w.configure(state=DISABLED)
        self.entry.configure(state=NORMAL)
        self.entry.delete(0,END)
        self.entry.configure(state=DISABLED)
        self.p.configure(state=NORMAL)
        self.p.delete(0.0, END)
        self.p.configure(state=DISABLED)
        self.q.configure(state=NORMAL)
        self.q.delete(0.0, END)
        self.q.configure(state=DISABLED)



    def confirm(self):
        self.answer = askyesno(title='Confirmation',message='Are you sure that you want to quit?')
        if self.answer:
            self.master.destroy()
            self.data.clear_file()

    def next(self):
        self.counter+=1
        if self.counter == 1:
            self.data.add_msg(self.t.get(1.0, END))
            self.data.split("\n")
            self.data.print_msg()
            for i in range(self.data.size()-1):
                self.t.insert((i+1.0), "{}:  ".format(i+1))
            self.t.configure(state=DISABLED)

        if self.data.evaluate() == False:
            print("Error: No input detected.")
            tkinter.messagebox.showinfo("Error Message", "No input detected!")
            self.counter = 0
            self.t.configure(state=NORMAL)
            self.t.delete(0.0, END)
            return

        if self.counter < self.data.size():
            self.t.configure(state=NORMAL)
            self.t.tag_add("here", (float(self.counter)), (float(self.counter)+.75))
            self.t.tag_add("before", (float(self.counter)-1.0), (float(self.counter-1.0) + .75))
            self.t.tag_configure("before", background="white", foreground="black")
            self.t.tag_configure("here", background="black", foreground="green")
            self.t.configure(state=DISABLED)
            self.w.configure(state=NORMAL)
            try:
                self.s = self.data.lexer(self.data.get_el(self.counter-1))
            except IndexError:
                print("Nothing to lexify")
            try:
                self.parse_op = self.data.parse()
            except IndexError:
                print("Nothing more to parse")
            self.p.configure(state=NORMAL)
            self.p.insert(INSERT, "\n\n****START OF PARSE TREE FOR LINE: {}****\n\n".format(self.counter))
            self.p.insert(INSERT, self.parse_op)
            self.p.insert(INSERT, "\n\n****END OF PARSE TREE FOR LINE: {}****\n\n".format(self.counter))
            self.p.configure(state=DISABLED)
            self.parse_tr = self.data.parse_tree()
            if len(self.parse_tr) != 0:
                self.q.configure(state=NORMAL)
                self.q.insert(INSERT, "\n\n****START OF PARSE TREE FOR LINE: {}****\n\n".format(self.counter))
                self.q.insert(INSERT, self.parse_tr)
                self.data.clear_file()
                self.q.insert(INSERT, "\n\n****END OF PARSE TREE FOR LINE: {}****\n\n".format(self.counter))
                self.q.configure(state=DISABLED)
            if len(self.s) != 0:
                self.w.insert(INSERT, "\nSTART OF LEXER FOR LINE: {}\n\n".format(self.counter))
                self.w.insert(INSERT, self.s)
                self.w.insert(INSERT, "\nEND OF LEXER FOR LINE: {}\n".format(self.counter))
            self.w.configure(state=DISABLED)
            self.entry.configure(state=NORMAL)
            self.entry.delete(0, END)
            self.entry.insert(INSERT, self.counter)
            self.entry.configure(state=DISABLED)

        if self.counter >= self.data.size():
            print("Error: End of Input.")
            self.answer1 = askyesno(title='Confirmation', message='Reached end of input. Do you want to reset?')
            if self.answer1:
                self.reset()


if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = lexer_GUI(myTkRoot)
    myTkRoot.mainloop()
