from nltk.chat.util import Chat, reflections

mypairs = [
    ['(hi|hello|hey|hallo|holla|hola)', ['hey there', 'hi there', 'haayyy']],
    ['(.*) your name ?', ['my name is CANKAYA BOT']],
    ['(.*)help(.*)',['I can help you']],
    ['how can I get documents?',['you can send an e-mail to oim@cankaya.edu.tr']],
    ['how can I see my exam results?',['you can see the exam results at http://sql.cankaya.edu.tr']],
    ['how much is the school fee?',['you can see the school fee at http://oim.cankaya.edu.tr/wp-content/uploads/sites/2/2021/06/2020_yili_ucret_bilgileri_11Guz.pdf']],
    ['how can i reach my advisor?',['you can call the department secretary.']],
    ['(engin|engineer|engineering)', ['0 312 233 13 84']],
    ['(law|faculty of law)', ['0 312 284 45 00']],
    ['(art|science|arts and sciences)', ['0 312 233 14 10']],
    ['(by|bye|bye bye)', ['have a nice day']],
]

myreflections = {
    'how are you':'fine',
    'I':'you',
    'my':'your',
    'mine':'yours'
}

chat = Chat(mypairs, myreflections)

chat.converse(quit='end')
