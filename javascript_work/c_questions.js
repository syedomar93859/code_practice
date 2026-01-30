let c_question_1 = {
    language: 'C',
    type: 'Written',
    question: 'How to print "Hello, World!"',
    answer: 'printf("Hello, World!");',
};

let c_question_2 = {
    language: 'C',
    type: 'Multiple Choice',
    question: 'What does the following declaration mean: <br> const int *p;',
    options: [
        'p is a pointer to a constant integer.',
        'p is a constant pointer to an integer.',
        'Both p and the integer are constant.',
        'The integer pointed to by p can be modified.'
    ],
    solution: 'p is a pointer to a constant integer.',
    randomize: function() {
        for (let i = this.options.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.options[i], this.options[j]] = [this.options[j], this.options[i]];
        }
    },
    
};

export function c_question_generator(){
    console.log(`Programming Language: C`);
    return [c_question_1, c_question_2];
};
