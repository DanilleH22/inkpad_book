/*
* @jest-environment jsdom
*/
 

const buttonClick = require("../script.js");

describe('showChapter function', () => {
    // Mock HTML elements
    document.body.innerHTML = `
        <div class="chapter" style="display: none;">Chapter 1</div>
        <div class="chapter" style="display: none;">Chapter 2</div>
        <div class="chapter" style="display: none;">Chapter 3</div>
        <button id="prevChapter" style="display: none;"></button>
        <button id="nextChapter"></button>
    `;

    const chapters = document.querySelectorAll('.chapter');
    const btnPrev = document.getElementById('prevChapter');
    const btnNext = document.getElementById('nextChapter');
    const totalChapters = chapters.length;

    // Test showChapter function
    test('should display the correct chapter and update button visibility', () => {
        // Define the function
        function showChapter(index) {
            chapters.forEach((chapter, idx) => {
                chapter.style.display = idx === index ? 'block' : 'none';
            });

            btnPrev.style.display = index > 0 ? 'block' : 'none';
            btnNext.style.display = index < totalChapters - 1 ? 'block' : 'none';
        }

        // Test for the first chapter
        showChapter(0);
        expect(chapters[0].style.display).toBe('block');
        expect(chapters[1].style.display).toBe('none');
        expect(btnPrev.style.display).toBe('none');
        expect(btnNext.style.display).toBe('block');

        // Test for the last chapter
        showChapter(totalChapters - 1);
        expect(chapters[totalChapters - 1].style.display).toBe('block');
        expect(chapters[totalChapters - 2].style.display).toBe('none');
        expect(btnPrev.style.display).toBe('block');
        expect(btnNext.style.display).toBe('none');
    });
});
