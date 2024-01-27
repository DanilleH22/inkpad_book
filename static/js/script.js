// ------------- Reading book ----------

    let currentChapter = 0;
    const chapters = document.querySelectorAll('.chapter');
    const totalChapters = chapters.length;

// Function to show the chapters
    function showChapter(index) {
        chapters.forEach((chapter, idx) => {
            chapter.style.display = idx === index ? 'block' : 'none';
        });
    }

// For clicking the next button - next chapter
    document.getElementById('nextChapter').addEventListener('click', function() {
        if (currentChapter < totalChapters - 1) {
            currentChapter++;
            showChapter(currentChapter);
        }
    });

// Clicking previous and going to previoius chapter
    document.getElementById('prevChapter').addEventListener('click', function() {
        if (currentChapter > 0) {
            currentChapter--;
            showChapter(currentChapter);
        }
    });

    // Initially show the first chapter
    showChapter(currentChapter);

