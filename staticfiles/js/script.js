document.addEventListener('DOMContentLoaded', function() {
    const chapters = document.querySelectorAll('.chapter');
    const btnPrev = document.getElementById('prevChapter');
    const btnNext = document.getElementById('nextChapter');

    if (!chapters.length || !btnPrev || !btnNext) {
        // Elements not found, exit the script
        return;
    }

    let currentChapterIndex = 0;
    const totalChapters = chapters.length;

    // Shows each chapter one at a time
    function showChapter(index) {
        // Update visibility of chapters
        chapters.forEach((chapter, idx) => {
            chapter.style.display = idx === index ? 'block' : 'none';
        });

        // Update button visibility
        btnPrev.style.display = index > 0 ? 'block' : 'none';
        btnNext.style.display = index < totalChapters - 1 ? 'block' : 'none';
    }

    // Next button - won't show on last chapter
    btnNext.addEventListener('click', function() {
        if (currentChapterIndex < totalChapters - 1) {
            currentChapterIndex++;
            showChapter(currentChapterIndex);
        }
    });

    // Previous button only show after 2nd chapter
    btnPrev.addEventListener('click', function() {
        if (currentChapterIndex > 0) {
            currentChapterIndex--;
            showChapter(currentChapterIndex);
        }
    });

    // Initially show the first chapter and set button visibility
    showChapter(currentChapterIndex);
    window.scrollTo(0, 0); // Scrolls to the top of the page
});
