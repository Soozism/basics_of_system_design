// System Design Tutorial Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Highlight active sidebar link
    const sidebarLinks = document.querySelectorAll('.sidebar a');
    const currentPath = window.location.pathname;
    
    sidebarLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath || 
            currentPath.includes(link.getAttribute('href'))) {
            link.classList.add('active');
        }
    });
    
    // Add fade-in animation to content
    const content = document.querySelector('.content');
    if (content) {
        content.classList.add('fade-in');
    }
    
    // Code syntax highlighting (basic)
    const codeBlocks = document.querySelectorAll('pre code');
    codeBlocks.forEach(block => {
        // Add line numbers
        const lines = block.innerHTML.split('\n');
        if (lines.length > 1) {
            block.innerHTML = lines.map((line, index) => 
                `<span class="line-number">${index + 1}</span>${line}`
            ).join('\n');
        }
    });
    
    // Search functionality
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            const searchResults = document.querySelector('.search-results');
            
            if (query.length > 2) {
                // Simple search implementation
                const content = document.querySelector('.content').textContent.toLowerCase();
                if (content.includes(query)) {
                    searchResults.innerHTML = '<p>Found matches in current page</p>';
                } else {
                    searchResults.innerHTML = '<p>No matches found</p>';
                }
                searchResults.style.display = 'block';
            } else {
                searchResults.style.display = 'none';
            }
        });
    }
    
    // Table of contents generation
    function generateTOC() {
        const headings = document.querySelectorAll('h2, h3, h4');
        const toc = document.querySelector('.table-of-contents');
        
        if (toc && headings.length > 0) {
            const tocList = document.createElement('ul');
            
            headings.forEach((heading, index) => {
                const id = `heading-${index}`;
                heading.id = id;
                
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = `#${id}`;
                a.textContent = heading.textContent;
                a.className = `toc-${heading.tagName.toLowerCase()}`;
                
                li.appendChild(a);
                tocList.appendChild(li);
            });
            
            toc.appendChild(tocList);
        }
    }
    
    generateTOC();
    
    // Print functionality
    const printBtn = document.querySelector('.print-btn');
    if (printBtn) {
        printBtn.addEventListener('click', function() {
            window.print();
        });
    }
    
    // Theme toggle (if needed)
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-theme');
            localStorage.setItem('theme', 
                document.body.classList.contains('dark-theme') ? 'dark' : 'light'
            );
        });
        
        // Load saved theme
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            document.body.classList.add('dark-theme');
        }
    }
    
    // Scroll to top button
    const scrollTopBtn = document.querySelector('.scroll-top');
    if (scrollTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                scrollTopBtn.style.display = 'block';
            } else {
                scrollTopBtn.style.display = 'none';
            }
        });
        
        scrollTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});

// Utility functions
function formatDate(date) {
    return new Date(date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        console.log('Copied to clipboard');
    });
}

// Add copy buttons to code blocks
document.addEventListener('DOMContentLoaded', function() {
    const codeBlocks = document.querySelectorAll('pre');
    
    codeBlocks.forEach(block => {
        const copyBtn = document.createElement('button');
        copyBtn.className = 'copy-btn';
        copyBtn.textContent = 'Copy';
        copyBtn.onclick = function() {
            copyToClipboard(block.textContent);
            copyBtn.textContent = 'Copied!';
            setTimeout(() => {
                copyBtn.textContent = 'Copy';
            }, 2000);
        };
        
        block.style.position = 'relative';
        copyBtn.style.position = 'absolute';
        copyBtn.style.top = '10px';
        copyBtn.style.right = '10px';
        copyBtn.style.padding = '5px 10px';
        copyBtn.style.fontSize = '12px';
        copyBtn.style.backgroundColor = '#f3f4f6';
        copyBtn.style.border = '1px solid #d1d5db';
        copyBtn.style.borderRadius = '4px';
        copyBtn.style.cursor = 'pointer';
        
        block.appendChild(copyBtn);
    });
});
