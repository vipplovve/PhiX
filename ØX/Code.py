import kivy
import mysql.connector as con
import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

bridge = con.connect(host='localhost', user='root', passwd='59123')
sql = bridge.cursor()
if bridge.is_connected():
    print('Successfully Connected To Server.')
sql.execute('create database if not exists CsProject;')
sql.execute('use CsProject;')


class Password(Screen):
    # BestAspectRatio=1.74
    Window.size = (813, 465)

    def check(self, n, p):
        n = self.ids.name.text
        p = self.ids.passw.text
        if n == 'Viplove' and p == 'PhiX':
            self.ids.name.text = ''
            self.ids.passw.text = ''
        else:
            print()
            print('YOU ARE NOT AUTHORISED TO ACCESS THIS PROGRAM! ')
            bridge.close()
            print('Disconnected From The Server.')
            quit()

    def bye(self):
        bridge.close()
        print('Disconnected From The Server.')
        quit()


class Menu(Screen):
    pass


class Calculator(Screen):

    def clear(self):
        self.ids.val.text = ''

    def use(self, b):
        x = self.ids.val.text
        if x == '0':
            self.ids.val.text = f'{b}'
        else:
            self.ids.val.text = f'{x}{b}'

    def add(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}+'

    def sub(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}-'

    def mul(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}*'

    def div(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}/'

    def factorial(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}!'

    def exp(self):
        x = self.ids.val.text
        self.ids.val.text = f'{x}^'

    def ans(self):
        x = self.ids.val.text
        if '+' in x:
            l = x.split('+')
            a = float(l[0])
            b = float(l[1])
            r = a + b
            r = round(r, 5)
            self.ids.val.text = str(r)

        elif '-' in x:
            l = x.split('-')
            a = float(l[0])
            b = float(l[1])
            r = a - b
            r = round(r, 5)
            self.ids.val.text = str(r)

        elif '*' in x:
            l = x.split('*')
            a = float(l[0])
            b = float(l[1])
            r = a * b
            r = round(r, 5)
            self.ids.val.text = str(r)

        elif '/' in x:
            l = x.split('/')
            a = float(l[0])
            b = float(l[1])
            if b != 0:
                r = a / b
                r = round(r, 5)
                self.ids.val.text = str(r)
            else:
                self.ids.val.text = 'ERROR'

        elif '!' in x:
            n = int(x[0])
            f = 1
            if n != 0:
                for i in range(1, n + 1):
                    f *= i
                self.ids.val.text = str(f)
            else:
                f = 1
                self.ids.val.text = str(f)

        elif '^' in x:
            l = x.split('^')
            a = float(l[0])
            b = float(l[1])
            r = a ** b
            r=round(r,5)
            self.ids.val.text = str(r)

    def inv(self):
        x = self.ids.val.text
        p = float(x)
        r = p ** -1
        r = round(r, 5)
        self.ids.val.text = (str(r))

    def slice(self):
        x = self.ids.val.text
        y = x[0:len(x) - 1]
        self.ids.val.text = y


class Log(Screen):

    def logarithm(self):
        a = float(self.ids.no.text)
        b = float(self.ids.baseval.text)
        ans = math.log(a, b)
        ans = round(ans, 5)
        self.ids.logval.text = f'{ans}'

    def antilogarithm(self):
        a = float(self.ids.logval.text)
        b = float(self.ids.baseval.text)
        ans = b ** a
        ans = round(ans, 5)
        self.ids.no.text = f'{ans}'

    def clear(self):
        self.ids.logval.text = ''
        self.ids.baseval.text = ''
        self.ids.no.text = ''


class Trigonometry(Screen):

    def sin(self):
        a = int(self.ids.theta.text)
        x = math.radians(a)
        ans = math.sin(x)
        ans = round(ans, 5)
        self.ids.trigo.text = f'{ans}'

    def cos(self):
        a = int(self.ids.theta.text)
        x = math.radians(a)
        ans = math.cos(x)
        ans = round(ans, 5)
        self.ids.trigo.text = f'{ans}'

    def tan(self):
        a = int(self.ids.theta.text)
        x = math.radians(a)
        ans = math.tan(x)
        ans = round(ans, 5)
        self.ids.trigo.text = f'{ans}'

    def cosec(self):
        a = int(self.ids.theta.text)
        x = math.radians(a)
        ans = math.sin(x)
        ans = 1 / ans
        ans = round(ans, 5)
        self.ids.trigo.text = f'{ans}'

    def sec(self):
        a = int(self.ids.theta.text)
        x = math.radians(a)
        ans = math.cos(x)
        ans = 1 / ans
        ans = round(ans, 5)
        self.ids.trigo.text = f'{ans}'

    def cot(self):
        a = int(self.ids.theta.text)
        x = math.radians(a)
        ans = math.tan(x)
        ans = 1 / ans
        ans = round(ans, 5)
        self.ids.trigo.text = f'{ans}'

    def clear(self):
        self.ids.theta.text = ''
        self.ids.trigo.text = ''


class Records(Screen):
    pass


class Insert(Screen):
    def clear(self):
        self.ids.rollno.text = ''
        self.ids.name.text = ''
        self.ids.cls.text = ''
        self.ids.fav.text = ''
        self.ids.wish.text = ''
        self.ids.popup.text = ''

    def insert(self):
        c = '''create table if not exists records
                (RollNo varchar(10),Name varchar(55),Class varchar(10),FavoriteAnime varchar(55),
                Wish varchar(55))
                            ;'''
        sql.execute(c)
        r = self.ids.rollno.text
        n = self.ids.name.text
        c = self.ids.cls.text
        f = self.ids.fav.text
        w = self.ids.wish.text
        c2 = "insert into records values('{}','{}','{}','{}','{}')"
        sql.execute(c2.format(r, n, c, f, w))
        bridge.commit()
        self.ids.popup.text = 'The Record Has Been Successfully Inserted!'


class Update(Screen):
    def clear(self):
        self.ids.rollno.text = ''
        self.ids.parameter.text = ''
        self.ids.newval.text = ''
        self.ids.check.text = ''
        self.ids.popup.text = ''

    def check(self):
        r = self.ids.rollno.text
        c3 = "select * from records where rollno='{}';"
        sql.execute(c3.format(r))
        a = sql.fetchone()
        self.ids.check.text = f'{a} \n This is The Corresponding Record'

    def update(self):
        r = self.ids.rollno.text
        p = self.ids.parameter.text
        n = self.ids.newval.text
        c4 = "update records set {}='{}' where rollno='{}'"
        sql.execute(c4.format(p, n, r))
        bridge.commit()
        self.ids.popup.text = 'The Record Has Been Successfully Updated! '


class Delete(Screen):
    def check(self):
        r = self.ids.rollno.text
        c3 = "select * from records where rollno='{}';"
        sql.execute(c3.format(r))
        a = sql.fetchone()
        self.ids.check.text = f'{a} \n This is The Corresponding Record'

    def clear(self):
        self.ids.rollno.text = ''
        self.ids.check.text = ''
        self.ids.popup.text = ''

    def delete(self):
        r = self.ids.rollno.text
        c4 = "delete from records where rollno='{}';"
        sql.execute(c4.format(r))
        bridge.commit()
        self.ids.popup.text = 'The Corresponding Record Has Been Successfully Deleted!'


class Search(Screen):
    def clear(self):
        self.ids.rollno.text = ''
        self.ids.result.text = ''

    def search(self):
        r = self.ids.rollno.text
        c5 = "select * from records where rollno='{}';"
        sql.execute(c5.format(r))
        ans = sql.fetchone()
        self.ids.result.text = f'The Required Record is: \n{ans}'


class Manager(ScreenManager):
    pass


a = Builder.load_file('Code.kv')


class MyGrid(Widget):
    pass


class ØX(App):
    def build(self):
        return a


ØX().run()
