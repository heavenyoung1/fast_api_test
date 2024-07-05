const leftIconsData = [
    { href: 'https://github.com', src: '/static/icons/github.png', alt: 'GitHub' },
    { href: 'https://instagram.com', src: '/static/icons/instagram.png', alt: 'Instagram' },
    { href: 'https://twitter.com', src: '/static/icons/x.png', alt: 'Twitter' },
    { href: 'https://linkedin.com', src: '/static/icons/VK.png', alt: 'VK' },
];

const rightIconsData = [
    { href: 'mailto:example@gmail.com', src: 'static/icons/email.png', alt: 'Email' },
];

function createIconElements(containerId, iconsData) {
    const container = document.getElementById(containerId);
    iconsData.forEach(iconData => {
        const anchor = document.createElement('a');
        anchor.href = iconData.href;
        anchor.target = '_blank';
        anchor.rel = 'noopener noreferrer';

        const img = document.createElement('img');
        img.src = iconData.src;
        img.alt = iconData.alt;

        anchor.appendChild(img);
        container.appendChild(anchor);
    });

    const line = document.createElement('div');
    line.className = 'line';
    container.appendChild(line);
}

createIconElements('left-icons', leftIconsData);
createIconElements('right-icons', rightIconsData);