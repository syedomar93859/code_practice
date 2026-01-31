let python_question_1 = {
    language: 'Python',
    type: 'Written',
    question: 'How to print "Hello, World!" in Python?',
    answer: 'print("Hello, World!")',
};

let python_question_2 = {
    language: 'Python',
    type: 'Written',
    question: 'Write a comment in Python with this text: This is a comment',
    answer: '# This is a comment',
};

let python_question_3 = {
    language: 'Python',
    type: 'Written',
    question: 'Write a variable x with the value of 11.',
    answer: 'x = 11',
};



export function python_question_generator(){
    console.log(`Programming Language: Python`);
    return [python_question_1, python_question_2, python_question_3];
};

