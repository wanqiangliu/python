#在函数存储在模块中,需要在函数名前加上 模块名.
import pizza_function
pizza_function.make_pizza(16,'pepperoni')
pizza_function.make_pizza(14,'mushrooms','green perpers','extra cheese')

#只导入模块中特定的函数,调用时直接写函数名即可
from pizza_function import make_pizza
make_pizza(18,'pepperoni')
make_pizza(20,'mushrooms','green perpers','extra cheese')

#使用as给函数指定别名
from pizza_function import make_pizza as mp
mp(32,'pepperoni')
mp(60,'mushrooms','green perpers','extra cheese')

#使用as给模块指定别名
import pizza_function as pf
pf.make_pizza(28,'peopernoi')
pf.make_pizza(66,'mushroom','green perpers','extra cheese')