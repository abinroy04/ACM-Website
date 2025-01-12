<!DOCTYPE html>
<html lang="en" x-data="{ darkMode: localStorage.getItem('darkMode') === null ? true : localStorage.getItem('darkMode') === 'true' }" 
      x-init="$watch('darkMode', val => localStorage.setItem('darkMode', val))"
      :class="{ 'dark': darkMode }">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='images/favicon-acm.ico') }}">
    <title>{% block title %}Saintgits ACM Student Chapter{% endblock %}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        dark: {
                            DEFAULT: '#1a1a1a',
                            secondary: '#242424'
                        }
                    }
                }
            }
        }
    </script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <style>
        @keyframes fadeSlideIn {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .page-content {
            animation: fadeSlideIn 0.6s ease-out forwards;
        }

        .stagger-animation > * {
            opacity: 0;
            animation: fadeSlideIn 0.5s ease-out forwards;
        }

        /* Static stagger delays */
        .stagger-animation > *:nth-child(1) { animation-delay: 0s; }
        .stagger-animation > *:nth-child(6) { animation-delay: 0.5s; }
        .stagger-animation > *:nth-child(11) { animation-delay: 1s; }
        .stagger-animation > *:nth-child(16) { animation-delay: 1.5s; }
        .stagger-animation > *:nth-child(20) { animation-delay: 1.9s; }

        .scroll-fade {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        }

        .scroll-fade.visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Delay variants for groups */
        .delay-100 { transition-delay: 0.1s; }
        .delay-200 { transition-delay: 0.2s; }
        .delay-300 { transition-delay: 0.3s; }
        .delay-400 { transition-delay: 0.4s; }
        .delay-500 { transition-delay: 0.5s; }

        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: 0;
            pointer-events: none;
            opacity: 0.4;
            visibility: visible;
            transition: opacity 0.3s ease;
        }

        .dark #particles-js {
            opacity: 0.6;
        }

        /* Ensure content appears above particles */
        header, main, footer {
            position: relative;
            z-index: 1;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col bg-gray-50 dark:bg-dark dark:text-gray-100">
    <div id="particles-js"></div>
    <!-- Navigation -->
    <header class="bg-white dark:bg-dark-secondary shadow-md">
        <nav class="max-w-7xl mx-auto pl-0 pr-2 sm:pl-1 sm:pr-4 lg:pl-2 lg:pr-6" x-data="{ isOpen: false }">
            <div class="flex justify-between h-24">
                <div class="flex items-center pl-1">
                    <a href="{{ url_for('home') }}" class="flex items-center">
                        <img src="{{ url_for('static', filename='images/logo.png') }}" 
                             alt="Logo" 
                             class="h-20 w-auto">
                    </a>
                </div>

                <!-- Dark mode toggle and Navigation -->
                <div class="flex items-center space-x-4">
                    <button @click="darkMode = !darkMode" 
                            class="p-2 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
                        <svg x-show="!darkMode" class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
                        </svg> 
                        <svg x-show="darkMode" class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
                        </svg>
                    </button>

                    <!-- Desktop Navigation -->
                    <div class="hidden md:flex md:items-center md:space-x-8">
                        <a href="{{ url_for('home') }}" 
                           class="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium"> <!-- Changed from text-sm to text-base -->
                            Home
                        </a>
                        <a href="{{ url_for('events') }}" 
                           class="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium">
                            Events
                        </a>
                        <a href="{{ url_for('team') }}" 
                           class="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium">
                            Our Team
                        </a>
                        <a href="{{ url_for('gallery') }}" 
                           class="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium">
                            Gallery
                        </a>
                        <a href="{{ url_for('contact') }}" 
                           class="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium">
                            Contact Us
                        </a>
                    </div>
                </div>

                <!-- Mobile menu button -->
                <div class="md:hidden flex items-center">
                    <button @click="isOpen = !isOpen" 
                            class="inline-flex items-center justify-center p-2 rounded-md text-gray-700 dark:text-gray-300 hover:text-gray-900 hover:bg-gray-100 focus:outline-none">
                        <svg class="h-6 w-6" x-show="!isOpen" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                        </svg>
                        <svg class="h-6 w-6" x-show="isOpen" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                        </svg>
                    </button>
                </div>
            </div>

            <!-- Mobile Navigation -->
            <div x-show="isOpen" class="md:hidden">
                <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                    <a href="{{ url_for('home') }}" 
                       class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium">
                        Home
                    </a>
                    <a href="{{ url_for('events') }}" 
                       class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium">
                        Events
                    </a>
                    <a href="{{ url_for('team') }}" 
                       class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium">
                        Our Team
                    </a>
                    <a href="{{ url_for('gallery') }}" 
                       class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium">
                        Gallery
                    </a>
                    <a href="{{ url_for('contact') }}" 
                       class="block text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 px-3 py-2 rounded-md text-base font-medium">
                        Contact Us
                    </a>
                </div>
            </div>
        </nav>
    </header>

    <!-- Main Content -->
    <main class="flex-grow">
        <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
            <div class="page-content">
                {% block content %}{% endblock %}
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white dark:bg-dark-secondary shadow-inner">
        <div class="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Contact Info -->
                <div class="space-y-4">
                    <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100">Contact Us</h3>
                    <div class="flex items-center space-x-2 text-gray-600 dark:text-gray-400">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                        </svg>
                        <span>+91 70250 05558</span>
                        <span>+91 83300 17090</span>
                    </div>
                    <div class="flex items-center space-x-2 text-gray-600 dark:text-gray-400">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                        </svg>
                        <a href="mailto:acm@saintgits.org" class="hover:text-blue-600 dark:hover:text-blue-400">acm@saintgits.org</a>
                    </div>
                </div>

                <!-- Quick Links -->
                <div class="space-y-4">
                    <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100">Quick Links</h3>
                    <div class="grid grid-cols-2 gap-4">
                        
                        <ul class="space-y-2 text-gray-600 dark:text-gray-400">
                            <li><a href="{{ url_for('events') }}" class="hover:text-blue-600 dark:hover:text-blue-400">Events</a></li>
                            <li><a href="{{ url_for('gallery') }}" class="hover:text-blue-600 dark:hover:text-blue-400">Gallery</a></li>
                            <li><a href="{{ url_for('contact') }}" class="hover:text-blue-600 dark:hover:text-blue-400">Contact</a></li>
                        </ul>
                        
                        <ul class="space-y-2 text-gray-600 dark:text-gray-400">
                            <li><a href="{{ url_for('team') }}" class="hover:text-blue-600 dark:hover:text-blue-400">Our Team</a></li>
                            <li><a href="{{ url_for('webmasters') }}" class="hover:text-blue-600 dark:hover:text-blue-400">Webmasters</a></li>
                        </ul>
                    </div>
                </div>

                <!-- Social Links -->
                <div class="space-y-4">
                    <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100">Follow Us</h3>
                    <div class="flex space-x-4">
                        <a href="https://www.linkedin.com/company/saintgits-acm-student-chapter" target="_blank" rel="noopener noreferrer" 
                           class="text-gray-600 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400">
                            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                            </svg>
                        </a>
                        <a href="https://www.instagram.com/acm.saintgits" target="_blank" rel="noopener noreferrer"
                           class="text-gray-600 dark:text-gray-400 hover:text-pink-600 dark:hover:text-pink-400">
                            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
            <div class="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700">
                <p class="text-center text-gray-600 dark:text-gray-400 text-sm">
                    &copy; 2025 Saintgits ACM Student Chapter. All rights reserved.
                </p>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            };

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        // Stop observing after animation
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);

            // Observe all elements with scroll-fade class
            document.querySelectorAll('.scroll-fade').forEach(element => {
                observer.observe(element);
            });
        });

        const lightParticleConfig = {
            // Configuration for light theme
            particles: {
                number: { value: 80, density: { enable: true, value_area: 800 } },
                color: { value: "#314259" }, // Gray color for light theme
                shape: { type: "circle" },
                opacity: { value: 0.3, random: false },
                size: { value: 3, random: true },
                line_linked: { enable: false },
                move: {
                    enable: true,
                    speed: 2,
                    direction: "none",
                    random: true,
                    straight: false,
                    out_mode: "out",
                    bounce: false
                }
            },
            interactivity: {
                detect_on: "canvas",
                events: {
                    onhover: { enable: true, mode: "bubble" },
                    onclick: { enable: true, mode: "push" },
                    resize: true
                },
                modes: {
                    bubble: {
                        distance: 150,
                        size: 6,
                        duration: 0.3,
                        opacity: 0.6,
                        speed: 3
                    },
                    push: { particles_nb: 4 }
                }
            },
            retina_detect: true
        };

        const darkParticleConfig = {
            // Configuration for dark theme
            particles: {
                number: { value: 80, density: { enable: true, value_area: 800 } },
                color: { value: "#6366f1" }, // Indigo color for dark theme
                shape: { type: "circle" },
                opacity: { value: 0.6, random: false },
                size: { value: 3, random: true },
                line_linked: { enable: false },
                move: {
                    enable: true,
                    speed: 2,
                    direction: "none",
                    random: true,
                    straight: false,
                    out_mode: "out",
                    bounce: true
                }
            },
            interactivity: {
                detect_on: "canvas",
                events: {
                    onhover: { enable: true, mode: "bubble" },
                    onclick: { enable: true, mode: "push" },
                    resize: true
                },
                modes: {
                    bubble: {
                        distance: 150,
                        size: 6,
                        duration: 0.3,
                        opacity: 0.8,
                        speed: 3
                    },
                    push: { particles_nb: 4 }
                }
            },
            retina_detect: true
        };

        function initParticles() {
            const particlesElement = document.getElementById('particles-js');
            const isDarkMode = document.documentElement.classList.contains('dark');
            
            // Clean up existing particles
            if (window.pJSDom && window.pJSDom.length) {
                window.pJSDom[0].pJS.fn.vendors.destroypJS();
                window.pJSDom = [];
            }
            particlesElement.innerHTML = '';

            // Initialize particles with appropriate config
            particlesJS('particles-js', isDarkMode ? darkParticleConfig : lightParticleConfig);
            particlesElement.style.visibility = 'visible';
            particlesElement.style.opacity = isDarkMode ? '0.6' : '0.4';
        }

        document.addEventListener('DOMContentLoaded', function() {
            // Initial setup
            initParticles();
            
            // Watch for theme changes using Alpine.js
            if (typeof Alpine !== 'undefined') {
                Alpine.effect(() => {
                    initParticles();
                });
            }

            // Additional theme change listener
            const html = document.documentElement;
            const observer = new MutationObserver((mutations) => {
                mutations.forEach((mutation) => {
                    if (mutation.attributeName === 'class') {
                        initParticles();
                    }
                });
            });

            observer.observe(html, {
                attributes: true,
                attributeFilter: ['class']
            });

        });

        // Handle page visibility changes
        document.addEventListener('visibilitychange', function() {
            if (document.visibilityState === 'visible' && document.documentElement.classList.contains('dark')) {
                initParticles();
            }
        });
    </script>
</body>
</html>
