# Anaconda-Fly-Jupyter
Jupyter notebooks are awesome

# Python IPython Jupyter Notebooks Matplotlib etc
..репозиторий нужен за ради "похвастаться", я тут вроде как на работу собрался устраиваться.

# Вот и давайте познакомимся.

Всем привет! 

У меня разруха в голове, но сегодня я решил отбросить свой страх и признать себя таким, какой я есть. Всю свою жизнь я боялся, что люди буду плохо относиться ко мне и старался нравиться всем, стремился всем угодить и быть идеальным. Пожалуй - с меня хватит. Объявляю этот аккаунт своей территорией - не зависимой от моих страхов, которые связаны с тем "что люди будут думать обо мне". Надоело.  

Поэтому, пользуйтесь важным приложением к материалам репозитория: https://youtu.be/HSOtku1j600
И.. если вам не нравяться программисты Python которые любят аниме - пользуйтесь крестиком справа 

Лично я вместо крестика советую использовать это https://youtu.be/u-WGS66ykD0

..или это: https://soundcloud.com/nekopandaneko/scarboroughfair

# Репозиторий повествует о божественности Anaconda и Jupyter Notebooks 

Anaconda это вещь! https://docs.continuum.io/anaconda/
Она открывает вам дверь на бескрайние поля Юпитера.
http://jupyter.readthedocs.io/en/latest/index.html
И объединяет возможности Python и Ipython 

Знакомство с этим праздником лучше начинать тут
https://habrahabr.ru/company/ods/blog/323210/

Всё вместе это окружение - которое даёт вам возможность работать с данными дата фрейма не только "для себя", но и для других. Если в вашей студии есть закладка Anaconda Interactive - вы как бог! Эта штука одинаково хорошо работает на Python и IPython и позволяет совместить возможности обоих языков без проблем. 

Я пишу код на Python 3.6 в VS 2015 - а Anaconda строит мне график и выводит его на экран уже средствами IPython и при этом мне не нужно беспокоиться о синтаксисе: любой скрипт написанный на Python 3 в студии можно выполнить в Anaconda Interactive как обычный код Python, а можно скормить его Юпитеру и обработать в рамках логики IPython.  

"Тетрадки Юпитер" - эта таже консоль Anaconda Interactive в студии, только полностью на IPython. окружение крутиться на localhoste внутри браузера и свободно обрабатывает любой код Python 3, который вы захотите ему скормить. Можно не заморачиваться и копипастить код Python 3 по шагам в cell - Юпитер поймёт и обработает.

Но! 

В отличии от студии Юпитер возвращает вам все графики, все таблицы и все результаты на том же экране и на самом видном месте! Их можно распечатать или сохранить в нескольких приятных для глаз форматах. Более того, можно с лёгкостью обмениваться результатами data mining с любыми людьми, которые "космически далеки" не только от аниме, но и от использования консоли. Юпитер умеет сохранять результаты вывода в HTML. 

Что фактически означает возможность спамить менеджеров и "аналитиков" сводными таблицами и графиками по одному нажатию кнопки. Все эти персонажи(коллеги) смогут получать от вас HTML файлы, которые им останеться только открыть в своём браузере и дивиться чуду дивному.

# При чём здесь репозиторий?  
- лучше один раз попробовать.
- мне нравятся тетрадки Юпитер.

Все файлы репозитория в формате HTML - это экспорт готовых результатов из Jupyter notebooks. Все файлы формата .py - исходники. Я использовал несколько "известных всем" датафреймов поскольку только учусь и других у меня нет. Если захотите исполнять код в консоли - не забудьте скачать соотвествующие файлы с данными и изменить путь к файлу на чтение. (хотя вы и так наверное об этом знаете, иначе не зашли бы на GitHub).

- Titanic Intro: проcтая демонстрация основ при работе со списком пассажиров Титаника.
- Matplotlib True: простая демонстрация возможностей визуализации фукнционала Matplotlib
- Heresy Lesson1 Telecom: хороший пример того, как Юпитер улучшает читабельность длиннокода.
- Homework lesson1 Adult: история про то - сколько таблиц влазит в Юпитер и как их потом читать.
- DFMatplotlib Adult: история про то - сколько графиков можно запихнуть в Юпитер и как это выглядит.

# http://coub.com/view/t0gud

# Лайфхак конвертации Python в IPython

Помимо того, что Юпитер позволяет положить на рабочий стол менеджера интерактивный HTML файл, который открывается в браузере в один клик без использования интерпретатора; - Юпитер генерит полезный лайфхак. 

Позволяет конвертировать код Python в IPython.

Исходный код всех скриптов данного репозитория был написан на Python 3.6 внутри студии и ручками ( логическая операция == cell ) откопирован в Jupyter notebook для последующего исполнения и удобства просмотра результатов. 

Поскольку исполнение кода внутри Юпитера происходит в рамках логики интерпретатора IPython то и последующий экспорт файлов при нажатии кнопки download as Python.py приводит к созданию файла в формате IPython. 

Таким образом мне совсем не обязательно обмазываться знанием о синтаксисе IPython (за исключением случаев "как запускать matplotlib" и т.п) если на выходе нужен именно он, достаточно знаний Python 3 и Юпитер.

# Зачем это нужно?

Благодаря Anaconde с Юпитером с одного скрипта написанного на Python 3 в студии вы получаете 1 файл HTML и 1 файл .py в IPython. Если немного включить голову, то рабочий процесс можно построить так:

- пишем код на Python 3 в студии с помощью всплывающих подсказок и проверки синтаксиса под Anaconda.
- транслируем код Python 3 из студии в тетрадки Юпитер и наслаждаемся читабельным результатом.  
- визуализируем через Юпитер в HTML и конвертируем в IPython для последующей раздачи коллегам.
- результаты визуализации отдаём менеджерам на "почитать".
- файлики с IPython отдаём коллегам на "подумать".

Смысл в том, что код написаный в студии в рамках задачи по датамайнингу - это длиннокод.

И чем шире задача, тем сложнее его читать. См.например: 

https://github.com/HorusHeresyHeretic/Learning-Python-from-zero/blob/master/Lesson-8/MachineLearning1.py

Небольшая ревизия содержимого датафрейма содержащая попытку "понять" основные индикаторы это порядка 200+ строк кода, который особо не откомментрируешь; места не хватит. В студии интерпретатор при работе с датафреймом возвращает 100500 строк, столбцов и значений на пару строк нашего кода - возвращаемые результаты просто некуда записать. Юпитер решает эту проблему путём сохранения в читабельном виде результатов предыдущих обращений.

В иделае это 2 монитора: в первом студия и разработка, во втором Юпитер с уже полученными результатами в качетве подсказки. Плюс - коллегам будет проще читать ваш код в формате IPython где он разбит по операциям.

Ну, как бы няши - я намекаю, что сокращение усилий на навигацию по результатам обращений к дата фрейму существенно импрувит процесс. Разглядывать то, что возвращает интерпретатор в студии, если речь идёт о результатах полученных например через .groupby в отношении 10-20 столбцов как бы "не очень". Это стоит определённых ресурсов и времени. 

Лучше потратить и то и другое на "подумать" над кодом - чем ломать голову в попытках соотнести то, что вернул интрепретатор сейчас с тем, что он вернул 400 строк вывода назад. Поэтому, я считаю правильным разглядывать результаты вывода в Юпитере.
