const questions = {
  "print(คำสั่งปริ้นออกมา)": "print",
  "loop(คำสั่งวนลูบเพื่อแสดง)": "loop",
  "import(คำสั่งนำอินเดอร์เครเตอร์เข้ามา)": "import",
  "def(สร้างฟังก์ชัน)": "def"
};

let currentQuestion = "";
let correctAnswer = "";
let score = 0;
let timeLeft = 10;
let timerInterval;

const questionBox = document.getElementById("question");
const answerInput = document.getElementById("answer");
const resultBox = document.getElementById("result");
const scoreBox = document.getElementById("score");
const timerBox = document.getElementById("timer");

function nextQuestion() {
  const keys = Object.keys(questions);
  currentQuestion = keys[Math.floor(Math.random() * keys.length)];
  correctAnswer = questions[currentQuestion];
  questionBox.textContent = currentQuestion;
  answerInput.value = "";
  resultBox.textContent = "";
  timeLeft = 10;
  timerBox.textContent = `เวลา: ${timeLeft}`;
  clearInterval(timerInterval);
  timerInterval = setInterval(updateTimer, 1000);
}

function updateTimer() {
  timeLeft--;
  timerBox.textContent = `เวลา: ${timeLeft}`;
  if (timeLeft === 0) {
    clearInterval(timerInterval);
    resultBox.textContent = `หมดเวลา! คำตอบที่ถูกต้องคือ '${correctAnswer}'`;
    score = 0;
    scoreBox.textContent = `คะแนน: ${score}`;
    setTimeout(nextQuestion, 2000);
  }
}

answerInput.addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    checkAnswer();
  }
});

function checkAnswer() {
  if (timeLeft > 0) {
    const userAnswer = answerInput.value.trim().toLowerCase();
    if (userAnswer === correctAnswer.toLowerCase()) {
      resultBox.textContent = "คำตอบถูกต้อง!";
      score++;
    } else {
      resultBox.textContent = `คำตอบผิด! คำตอบที่ถูกต้องคือ '${correctAnswer}'`;
      score = 0;
    }
    scoreBox.textContent = `คะแนน: ${score}`;
    clearInterval(timerInterval);
    setTimeout(nextQuestion, 2000);
  }
}

window.onload = nextQuestion;
