import random
def gen_pass():
chars = &quot;abcdefghijklmnopqstuvwxyz&quot;
num = &quot;1234567890&quot;
symbol = &quot;!@#$%^&amp;*~&quot;
def creat_pass1():
print(&quot;Here is Your Password List --&gt;&quot;)
for pwd in range(globals()[&#39;number&#39;]):
password = &#39;&#39;
for c in range(globals()[&#39;length&#39;]):
password += random.choice(chars +
num + symbol)
print(pwd + 1, &quot; -&gt; &quot;, end=&quot;&quot;)
print(password)
def creat_pass2():
print(&quot;Here is Your Password List --&gt;&quot;)
for pwd in range(globals()[&#39;number&#39;]):
password = &#39;&#39;
for c in range(globals()[&#39;length&#39;]):
password += random.choice(chars)
print(pwd + 1, &quot; -&gt; &quot;, end=&quot;&quot;)
print(password)
print(&quot;Note : These Password is Just Using
the Charachters So it Not So Secure&quot;)
def creat_pass3():
print(&quot;Here is Your Password List --&gt;&quot;)
for pwd in range(globals()[&#39;number&#39;]):
password = &#39;&#39;
for c in range(globals()[&#39;length&#39;]):
password += random.choice(chars +
num)
print(pwd + 1, &quot; -&gt; &quot;, end=&quot;&quot;)
print(password)
print(&quot;Note : The Password is Using
Character and Number so Security is Medium&quot;)

def creat_pass4():
print(&quot;Here is Your Password List --&gt;&quot;)
for pwd in range(globals()[&#39;number&#39;]):
password = &#39;&#39;
for c in range(globals()[&#39;length&#39;]):
password += random.choice(chars +
symbol)
print(pwd + 1, &quot; -&gt; &quot;, end=&quot;&quot;)
print(password)
print(&quot;Note : The Password is Using
Character and Symbol so Security is Medium&quot;)
def func_call():
number = input(&#39;number of password ? -&gt; &#39;)
globals()[&#39;number&#39;] = int(number)
globals()[&#39;length&#39;] = int(input(&#39;What the
length of Your Password ? -&gt;&#39;))
ask1 = input(&quot;Wants to include Numbers on
To Your Password ? [ yes or no] --&gt; &quot;)
ask2 = input(&quot;Wants to include Symbol on
to your Password ? [yes or no ] --&gt; &quot;)
if ask1 == &#39;yes&#39; and ask2 == &#39;yes&#39;:
creat_pass1()
ask3 = input(&quot;Want to Try Again ? -&gt; &quot;)
if ask3 == &#39;yes&#39;:
func_call()
else:
print(&quot;Okk Thank You For Using These
Programm&quot;)
print(
&quot;Note :- Dont Use These Passwords
for Facebook or Any Other Social Link Platform
Use is For Wifi or Basic Things &quot;)
elif ask1 == &#39;no&#39; and ask2 == &#39;no&#39;:
creat_pass2()
ask3 = input(&quot;Want to Try Again ? -&gt; &quot;)

4

if ask3 == &#39;yes&#39;:
func_call()
else:
print(&quot;Okk Thank You For Using These
Programm&quot;)
print(
&quot;Note :- Dont Use These Passwords
for Facebook or Any Other Social Link Platform
Use is For Wifi or Basic Things &quot;)
elif ask1 == &quot;yes&quot; and ask2 == &quot;no&quot;:
creat_pass3()
ask3 = input(&quot;Want to Try Again ? -&gt; &quot;)
if ask3 == &#39;yes&#39;:
func_call()
else:
print(&quot;Okk Thank You For Using These
Programm&quot;)
print(
&quot;Note :- Dont Use These Passwords
for Facebook or Any Other Social Link Platform
Use is For Wifi or Basic Things &quot;)
elif ask1 == &#39;no&#39; and ask2 == &quot;yes&quot;:
creat_pass4()
ask3 = input(&quot;Want to Try Again ? -&gt; &quot;)
if ask3 == &#39;yes&#39;:
func_call()
else:
print(&quot;Okk Thank You For Using These
Programm&quot;)
print(
&quot;Note :- Dont Use These Passwords
for Facebook or Any Other Social Link Platform
Use is For Wifi or Basic Things &quot;)
else:
print(&quot;&lt;-- Not a Valid statement --&gt;&quot;)
ask3 = input(&quot;Want to Try Again ? -&gt; &quot;)
if ask3 == &#39;yes&#39;:
func_call()
else:
print(&quot;Okk Thank You For Using These
Programm&quot;)
print(
&quot;Note :- Dont Use These Passwords
for Facebook or Any Other Social Link Platform
Use is For Wifi or Basic Things &quot;)
func_call()

start()

def cre_pass():
print(&quot;&lt;------Welcome To ------&gt;&quot;)
print(&quot;&lt;-- Password Security --&gt;&quot;)
print(&quot;Note : We Are Store Your Password in
Your File But we Are not assigning Password For
Your File Consider Your File Name Should be
Unique&quot;)
def cre_pass1():
print(&quot;&quot;)
name=input(&quot;Whats the Name of Your File?
-&gt; &quot;)
my_file = open(name, &quot;a&quot;)
x=input(&quot;Enter The Number of Your Pass -&gt;
&quot;)
que1=input(&quot;Enter Your Name of Password
-&gt; &quot;)
que2=input(&quot;Enter Your Password -&gt; &quot;)
my_file.write(&quot;\n&quot;+ x +&quot; &quot;+ que1 + &quot; : &quot; +
que2 + &quot;\n&quot; )
my_file.close()
my_file = open(name,&quot;r&quot;)
print(&quot;&quot;)
print(&quot;Here You are Saving &quot;)
print(my_file.read())

cre_pass1()
ask6=input(&quot;Whant to Enter One More
password ? [yes or no] -&gt; &quot;)
if ask6 == &#39;yes&#39;:
cre_pass1()
else :
print(&quot;Thanks We Are Try to Secure Your
Password&quot;)
start()

def check_pass():
print(&quot;&lt;--- lets Check Your Passwords --&gt;&quot;)
name=input(&quot;Enter Your File Name -&gt;&quot;)
my_file = open(name, &quot;r&quot;)
print(&quot;&quot;)

5

print(&quot;Here You are Saving &quot;)
print(my_file.read())
my_file.close()
start()

def start():
print(&quot;&lt;--- Choose Any Option --&gt;&quot;)
print(&quot;1.Secure Your Password &quot;)
print(&quot;2.Check Your Password &quot;)
print(&quot;3.Generate a password&quot;)
ask4=int(input(&quot;What Do You Want to Do
?&quot;))
if ask4 == 1 :
cre_pass()
elif ask4 == 2:
check_pass()
elif ask4 == 3:
gen_pass()
elif ask4 == 4:
pass
else :
print(&quot;You Are not Choose A Valid Number
Re-Run These Programm&quot;)
start()
