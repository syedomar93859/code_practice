let java_question_1 = {
    language: 'Java',
    type: 'Written',
    question: 'How to print "Hello, World!" in Java?',
    answer: 'System.out.println("Hello, World!");',
};

let java_question_2 = {
    language: 'Java',
    type: 'Multiple Choice',
    question: 'What does the "void" keyword indicate in Java?',
    options: [
        'It indicates that a method does not return a value.',
        'It indicates that a method returns a value.',
        'It indicates that a method is private.',
        'It indicates that a method is static.'
    ],
    solution: 'It indicates that a method does not return a value.',
    randomize: function() {
    for (let i = this.options.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [this.options[i], this.options[j]] = [this.options[j], this.options[i]];
        }
    },

};

export function java_question_generator(){
    console.log(`Programming Language: Java`);
    return [java_question_1, java_question_2];
};
