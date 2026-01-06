// Repeater data rendering system
// Loads repeaters.json and renders different views for different pages

let repeatersData = null;

// Load repeater data from JSON file
async function loadRepeaterData() {
    try {
        const response = await fetch('repeaters.json');
        repeatersData = await response.json();
        return repeatersData;
    } catch (error) {
        console.error('Error loading repeater data:', error);
        return null;
    }
}

// Format frequency with offset
function formatFrequency(repeater) {
    const toneDisplay = repeater.toneText || repeater.tone;
    return `${repeater.frequency}${repeater.offset} (${toneDisplay}${repeater.tone && !repeater.toneText ? ' Tone' : ''})`;
}

// Format frequency with callsign
function formatFrequencyWithCallsign(repeater) {
    return `${repeater.frequency}${repeater.offset} (${repeater.tone}) • ${repeater.callsign}`;
}

// Get status class and text
function getStatusDisplay(repeater) {
    const statusText = repeater.statusText || repeater.status.charAt(0).toUpperCase() + repeater.status.slice(1);
    return { class: repeater.status, text: statusText };
}

// Get link type class and text
function getLinkTypeDisplay(repeater) {
    const linkTypeLabels = {
        'fulltime': 'Full-Time',
        'parttime': 'Part-Time',
        'skywarn': 'SKYWARN'
    };
    return {
        class: repeater.linkType,
        text: linkTypeLabels[repeater.linkType] || repeater.linkType
    };
}

// Render simple list item (for index.html style)
function renderSimpleListItem(repeater) {
    const status = getStatusDisplay(repeater);
    const linkType = getLinkTypeDisplay(repeater);
    const location = repeater.locationShort || repeater.location;

    return `
        <li class="repeater-item">
            <span class="repeater-name">${location}</span>
            <span class="repeater-frequency">${formatFrequency(repeater)}</span>
            <span class="status ${status.class}">${status.text}</span>
            <span class="linktype ${linkType.class}">${linkType.text}</span>
        </li>
    `;
}

// Render detailed list item (for repeaters.html style)
function renderDetailedListItem(repeater) {
    const status = getStatusDisplay(repeater);
    const linkType = getLinkTypeDisplay(repeater);
    const location = repeater.locationDetail ? `${repeater.location.split('(')[0].trim()} (${repeater.locationDetail})` : repeater.location;

    let detailsHTML = '<li style="margin-left: 20px; padding: 10px;';

    // Special styling for hub and historic repeaters
    if (repeater.isHub) {
        detailsHTML += ' background-color: #f0f8ff; border-left: 3px solid var(--primary-blue);">';
    } else if (repeater.features && repeater.features.includes('Historic')) {
        detailsHTML += ' background-color: #fff8dc; border-left: 3px solid var(--green-accent);">';
    } else {
        detailsHTML += '">';
    }

    // Add features/special notes
    if (repeater.isHub) {
        detailsHTML += '<strong>System Hub Repeater</strong> - All intertie traffic is processed through this UHF hub<br>';
        detailsHTML += '<em>Features: Emergency power generator with automatic transfer switch</em><br>';
    } else if (repeater.features && repeater.features.includes('Historic')) {
        detailsHTML += '<strong>Historic Repeater</strong> - One of the oldest repeaters in Georgia<br>';
    } else if (repeater.features) {
        detailsHTML += `<strong>Features:</strong> ${repeater.features}<br>`;
    }

    if (repeater.coverage) {
        detailsHTML += `<strong>Coverage:</strong> ${repeater.coverage}<br>`;
    }

    if (repeater.sponsor) {
        detailsHTML += `<strong>Sponsor${repeater.sponsor.includes(' and ') || repeater.sponsor.includes(',') ? 's' : ''}:</strong> ${repeater.sponsor}<br>`;
    }

    if (repeater.club) {
        detailsHTML += `<strong>Club:</strong> ${repeater.club}<br>`;
    }

    if (repeater.function) {
        detailsHTML += `<strong>Function:</strong> ${repeater.function}`;
    }

    detailsHTML += '</li>';

    return `
        <li class="repeater-item" id="${repeater.id}">
            <span class="repeater-name">${location}</span>
            <span class="repeater-frequency">${formatFrequencyWithCallsign(repeater)}</span>
            <span class="status ${status.class}">${status.text}</span>
            <span class="linktype ${linkType.class}">${linkType.text}</span>
        </li>
        ${detailsHTML}
    `;
}

// Render table row for quick reference
function renderTableRow(repeater, index) {
    const status = getStatusDisplay(repeater);
    const linkType = getLinkTypeDisplay(repeater);
    const location = repeater.locationShort || repeater.location;
    const bgColor = index % 2 === 0 ? '' : ' style="background-color: #f9f9f9;"';

    return `
        <tr${bgColor}>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>${repeater.frequency}${repeater.offset}</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;"><a href="#${repeater.id}" style="color: var(--primary-blue); text-decoration: none;">${location}</a></td>
            <td style="padding: 8px; border: 1px solid #ddd;">${repeater.tone}</td>
            <td style="padding: 8px; border: 1px solid #ddd;">${repeater.callsign || 'N/A'}</td>
            <td style="padding: 8px; border: 1px solid #ddd; text-align: center;"><span class="status ${status.class}">${status.text}</span> <span class="linktype ${linkType.class}">${linkType.text}</span></td>
        </tr>
    `;
}

// Render repeater list for index.html
function renderIndexRepeaters() {
    if (!repeatersData) return;

    const fullTimeRepeaters = repeatersData.repeaters.filter(r => r.linkType === 'fulltime');
    const partTimeRepeaters = repeatersData.repeaters.filter(r => r.linkType === 'parttime');
    const skywarnRepeaters = repeatersData.repeaters.filter(r => r.linkType === 'skywarn');

    // Render full time linked
    const fullTimeList = document.getElementById('fulltime-repeaters-list');
    if (fullTimeList) {
        fullTimeList.innerHTML = fullTimeRepeaters.map(renderSimpleListItem).join('');
    }

    // Render part time linked
    const partTimeList = document.getElementById('parttime-repeaters-list');
    if (partTimeList) {
        partTimeList.innerHTML = partTimeRepeaters.map(renderSimpleListItem).join('');
    }

    // Render SKYWARN
    const skywarnList = document.getElementById('skywarn-repeaters-list');
    if (skywarnList) {
        skywarnList.innerHTML = skywarnRepeaters.map(renderSimpleListItem).join('');
    }
}

// Render repeater tables for repeaters.html
function renderRepeatersPage() {
    if (!repeatersData) return;

    // Sort repeaters alphabetically by location for the quick reference table
    const sortedRepeaters = repeatersData.repeaters
        .filter(r => r.linkType !== 'skywarn')
        .sort((a, b) => {
            const locA = (a.locationShort || a.location).toLowerCase();
            const locB = (b.locationShort || b.location).toLowerCase();
            return locA.localeCompare(locB);
        });

    // Render quick reference table
    const tableBody = document.getElementById('quick-reference-table');
    if (tableBody) {
        tableBody.innerHTML = sortedRepeaters.map((r, i) => renderTableRow(r, i)).join('');
    }

    // Render full time linked detailed list
    const fullTimeRepeaters = repeatersData.repeaters.filter(r => r.linkType === 'fulltime');
    const fullTimeDetailedList = document.getElementById('fulltime-detailed-list');
    if (fullTimeDetailedList) {
        fullTimeDetailedList.innerHTML = fullTimeRepeaters.map(renderDetailedListItem).join('');
    }

    // Render part time linked detailed list
    const partTimeRepeaters = repeatersData.repeaters.filter(r => r.linkType === 'parttime');
    const partTimeDetailedList = document.getElementById('parttime-detailed-list');
    if (partTimeDetailedList) {
        partTimeDetailedList.innerHTML = partTimeRepeaters.map(renderDetailedListItem).join('');
    }

    // Render SKYWARN list
    const skywarnRepeaters = repeatersData.repeaters.filter(r => r.linkType === 'skywarn');
    const skywarnList = document.getElementById('skywarn-detailed-list');
    if (skywarnList) {
        skywarnList.innerHTML = skywarnRepeaters.map(renderDetailedListItem).join('');
    }
}

// Initialize repeater display based on page
async function initRepeaters() {
    await loadRepeaterData();

    const currentPage = window.location.pathname.split('/').pop() || 'index.html';

    if (currentPage === 'index.html') {
        renderIndexRepeaters();
    } else if (currentPage === 'repeaters.html') {
        renderRepeatersPage();
    }
}

// Load repeaters when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initRepeaters);
} else {
    initRepeaters();
}
