import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(
    page_title="LabelBoxMini",
    page_icon="🧊",
    layout="wide")

components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Annotation Tool</title>
    <style>
        body {
            margin: 0;
            font-family: sans-serif;
            background-color: #e0e0e0;
            display: flex;
            height: 100vh;
            overflow: hidden; /* Prevent scrollbars */
        }

        /* Sidebar Styles */
        .sidebar {
            background-color: #343a40; /* Dark background */
            color: white;
            width: 250px;
            height: 100%;
            padding-top: 20px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
        }

        .sidebar-menu {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .sidebar-menu li {
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .sidebar-menu li.active,
        .sidebar-menu li:hover {
            background-color: #495057;
        }

        .sidebar-menu li i {
            margin-right: 10px;
        }

        .sidebar-content {
            flex-grow: 1;
            padding: 20px;
            overflow-y: auto; /* Allow scrolling for content */
        }

        .sidebar-content h4 {
            margin-top: 0;
        }

        .no-annotations {
            text-align: center;
            color: #aaa;
            padding: 20px;
        }

        /* Main Content Styles */
        .main-content {
            flex-grow: 1;
            background-color: #f8f9fa; /* Light background */
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .top-bar {
            background-color: #fff;
            padding: 10px 20px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .breadcrumbs {
            font-size: 14px;
            color: #6c757d;
        }

        .breadcrumbs span {
            margin-right: 5px;
        }

        .breadcrumbs span:not(:last-child)::after {
            content: '>';
            margin-left: 5px;
        }

        .image-navigation {
            display: flex;
            align-items: center;
        }

        .image-navigation button {
            background-color: transparent;
            border: none;
            cursor: pointer;
            margin: 0 10px;
            font-size: 16px;
            color: #007bff;
        }

        .image-area {
            flex-grow: 1;
            background-color: #ccc;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden; /* Clip content that overflows */
        }

        #annotation-image {
            max-width: 100%;
            max-height: 100%;
            display: block; /* Remove extra space below image */
        }

        .annotation-editor {
            position: absolute;
            top: 10px;
            left: 10px;
            background-color: #fff;
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
            z-index: 10; /* Ensure it's above the image */
        }

        .annotation-editor h5 {
            margin-top: 0;
            margin-bottom: 10px;
        }

        .annotation-editor input[type="text"] {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 3px;
            box-sizing: border-box;
        }

        .annotation-editor button {
            padding: 8px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            margin-right: 5px;
        }

        .annotation-editor button.delete {
            background-color: #dc3545;
        }

        .annotation-list {
            margin-top: 15px;
            border-top: 1px solid #eee;
            padding-top: 10px;
        }

        .annotation-item {
            display: flex;
            align-items: center;
            margin-bottom: 5px;
        }

        .annotation-item span {
            flex-grow: 1;
            font-size: 14px;
        }

        .annotation-item .color-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 5px;
        }

        /* Right Toolbar Styles */
        .right-toolbar {
            background-color: #343a40;
            color: white;
            width: 60px;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 20px;
            box-sizing: border-box;
        }

        .toolbar-button {
            background-color: transparent;
            border: none;
            color: white;
            font-size: 20px;
            margin-bottom: 15px;
            cursor: pointer;
            transition: opacity 0.3s ease;
        }

        .toolbar-button:hover {
            opacity: 0.7;
        }

        /* Bottom Bar Styles */
        .bottom-bar {
            background-color: #fff;
            padding: 10px 20px;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .zoom-controls {
            display: flex;
            align-items: center;
        }

        .zoom-controls button {
            background-color: transparent;
            border: 1px solid #ccc;
            border-radius: 3px;
            padding: 5px 10px;
            margin: 0 5px;
            cursor: pointer;
        }

        /* Annotation Box Styles */
        .annotation-box {
            position: absolute;
            border: 2px solid blue;
            box-sizing: border-box;
            cursor: move;
        }

        .annotation-box-label {
            position: absolute;
            top: -15px;
            left: 0;
            background-color: blue;
            color: white;
            padding: 2px 5px;
            font-size: 12px;
            border-radius: 3px;
        }

        /* Utility Classes */
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="sidebar">
        <ul class="sidebar-menu">
            <li class="active"><i class="fas fa-database"></i> Raw Data</li>
            <li><i class="fas fa-tag"></i> Labels</li>
            <li><i class="fas fa-sliders-h"></i> Attributes</li>
            <li><i class="far fa-comment-dots"></i> Comments</li>
            <li><i class="fas fa-history"></i> History</li>
        </ul>
        <div class="sidebar-content">
            <h4>Raw Data</h4>
            <div id="raw-data-content">
                <p class="no-annotations">No Annotations</p>
                <!-- Raw data content will be displayed here -->
            </div>
             <div id="labels-content" class="hidden">
                <h4>Labels</h4>
                <ul id="annotation-labels">
                    <!-- Annotation labels will be listed here -->
                </ul>
            </div>
            <div id="attributes-content" class="hidden">
                <h4>Attributes</h4>
                <p>No attributes defined.</p>
            </div>
            <div id="comments-content" class="hidden">
                <h4>Comments</h4>
                <p>No comments yet.</p>
            </div>
            <div id="history-content" class="hidden">
                <h4>History</h4>
                <p>No history available.</p>
            </div>
        </div>
    </div>

    <div class="main-content">
        <div class="top-bar">
            <div class="breadcrumbs">
                <span>CAR DETECTION</span><span>ANNOTATE</span><span>Cars Moving On Road Stock Footage - Free Download_mp4-0491...</span>
            </div>
            <div class="image-navigation">
                <button><</button>
                <span>108 / 303</span>
                <button>></button>
            </div>
        </div>

        <div class="image-area">
            <img id="annotation-image" src="https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/blogs/22606/images/b80886-de54-602b-81d2-f0425b17e04_shutterstock_668209624-1.jpeg" alt="Annotation Image">
            <div class="annotation-editor">
                <h5>Annotation Editor</h5>
                <input type="text" id="annotation-label" placeholder="Label">
                <button id="save-annotation">Save (Enter)</button>
                <button class="delete hidden" id="delete-annotation">Delete</button>
                <div class="annotation-list" id="annotation-list">
                    <!-- Existing annotations will be listed here -->
                </div>
            </div>
            <!-- Annotation boxes will be added here dynamically -->
        </div>

        <div class="bottom-bar">
            <div class="zoom-controls">
                <button id="zoom-out">-</button>
                <span id="zoom-level">100%</span>
                <button id="zoom-in">+</button>
                <button id="reset-zoom">RESET</button>
            </div>
            <div>
                <!-- Additional bottom bar elements -->
            </div>
        </div>
    </div>

    <div class="right-toolbar">
        <button class="toolbar-button"><i class="fas fa-hand-paper"></i></button>
        <button class="toolbar-button"><i class="far fa-square"></i></button>
        <button class="toolbar-button"><i class="fas fa-vector-square"></i></button>
        <button class="toolbar-button"><i class="fas fa-magic"></i></button>
        <button class="toolbar-button"><i class="fas fa-ruler-combined"></i></button>
        <button class="toolbar-button"><i class="fas fa-brush"></i></button>
        <button class="toolbar-button"><i class="fas fa-crop-alt"></i></button>
        <button class="toolbar-button"><i class="fas fa-sync-alt"></i></button>
        <button class="toolbar-button"><i class="far fa-comment-dots"></i></button>
        <button class="toolbar-button"><i class="fas fa-undo"></i></button>
        <button class="toolbar-button"><i class="fas fa-redo"></i></button>
        <button class="toolbar-button"><i class="fas fa-ban"></i></button>
    </div>

    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
    <script>
        const annotationImage = document.getElementById('annotation-image');
        const imageArea = document.querySelector('.image-area');
        const annotationEditor = document.querySelector('.annotation-editor');
        const annotationLabelInput = document.getElementById('annotation-label');
        const saveAnnotationButton = document.getElementById('save-annotation');
        const deleteAnnotationButton = document.getElementById('delete-annotation');
        const annotationList = document.getElementById('annotation-list');
        const rawDataContent = document.getElementById('raw-data-content');
        const annotationLabelsList = document.getElementById('annotation-labels');

        const sidebarItems = document.querySelectorAll('.sidebar-menu li');
        const sidebarContents = document.querySelectorAll('.sidebar-content > div');

        let annotations = [];
        let isDrawing = false;
        let startX, startY, currentBox;
        let selectedAnnotation = null;
        let zoomLevel = 1;
        const zoomStep = 0.1;
        const zoomLevelDisplay = document.getElementById('zoom-level');
        const zoomInButton = document.getElementById('zoom-in');
        const zoomOutButton = document.getElementById('zoom-out');
        const resetZoomButton = document.getElementById('reset-zoom');

        // Sample raw data (replace with actual data)
        const sampleRawData = {
            "accumulator": null,
            "annotation_jobs": [],
            "batches": [],
            "camera": null,
            "created": "...",
            "hashes": [],
            "height": 1080,
            "id": "...",
            "label": [
                "Unlabeled"
            ],
            "metadata": {}
        };

        function displayRawData(data) {
            rawDataContent.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        }

        function updateAnnotationLabelsList() {
            const labels = [...new Set(annotations.map(anno => anno.label))];
            annotationLabelsList.innerHTML = labels.map(label => `<li>${label}</li>`).join('');
        }

        function renderAnnotations() {
            // Clear existing annotation boxes
            document.querySelectorAll('.annotation-box').forEach(box => box.remove());

            annotations.forEach((anno, index) => {
                const box = document.createElement('div');
                box.classList.add('annotation-box');
                box.style.left = `${anno.x}px`;
                box.style.top = `${anno.y}px`;
                box.style.width = `${anno.width}px`;
                box.style.height = `${anno.height}px`;
                box.style.borderColor = anno.color;
                box.dataset.index = index;

                const label = document.createElement('div');
                label.classList.add('annotation-box-label');
                label.textContent = anno.label;
                box.appendChild(label);

                box.addEventListener('click', () => {
                    selectAnnotation(index);
                });

                imageArea.appendChild(box);
            });
            updateAnnotationList();
            updateAnnotationLabelsList();
        }

        function updateAnnotationList() {
            annotationList.innerHTML = '';
            annotations.forEach((anno, index) => {
                const item = document.createElement('div');
                item.classList.add('annotation-item');
                item.innerHTML = `
                    <span class="color-indicator" style="background-color: ${anno.color}"></span>
                    <span>${anno.label}</span>
                `;
                item.addEventListener('click', () => {
                    selectAnnotation(index);
                });
                annotationList.appendChild(item);
            });
             if (annotations.length > 0) {
                rawDataContent.querySelector('.no-annotations').classList.add('hidden');
            } else {
                rawDataContent.querySelector('.no-annotations').classList.remove('hidden');
            }
        }

        function selectAnnotation(index) {
            selectedAnnotation = index;
            const anno = annotations[index];
            annotationLabelInput.value = anno.label;
            annotationEditor.style.display = 'block';
            deleteAnnotationButton.classList.remove('hidden');
        }

        function deselectAnnotation() {
            selectedAnnotation = null;
            annotationLabelInput.value = '';
            annotationEditor.style.display = 'none';
            deleteAnnotationButton.classList.add('hidden');
        }

        function getRandomColor() {
            const letters = '0123456789ABCDEF';
            let color = '#';
            for (let i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }

        imageArea.addEventListener('mousedown', (e) => {
            if (e.target === annotationImage) {
                isDrawing = true;
                startX = e.offsetX;
                startY = e.offsetY;
                currentBox = document.createElement('div');
                currentBox.classList.add('annotation-box');
                currentBox.style.left = `${startX}px`;
                currentBox.style.top = `${startY}px`;
                currentBox.style.borderColor = getRandomColor();
                imageArea.appendChild(currentBox);
                deselectAnnotation();
            }
        });

        imageArea.addEventListener('mousemove', (e) => {
            if (!isDrawing) return;
            const currentX = e.offsetX;
            const currentY = e.offsetY;
            const width = Math.abs(currentX - startX);
            const height = Math.abs(currentY - startY);
            currentBox.style.width = `${width}px`;
            currentBox.style.height = `${height}px`;
            currentBox.style.left = `${Math.min(startX, currentX)}px`;
            currentBox.style.top = `${Math.min(startY, currentY)}px`;
        });

        imageArea.addEventListener('mouseup', (e) => {
            if (!isDrawing) return;
            isDrawing = false;
            const label = annotationLabelInput.value.trim() || 'Unlabeled';
            const color = currentBox.style.borderColor;
            annotations.push({
                x: parseInt(currentBox.style.left),
                y: parseInt(currentBox.style.top),
                width: parseInt(currentBox.style.width),
                height: parseInt(currentBox.style.height),
                label: label,
                color: color
            });
            imageArea.removeChild(currentBox);
            renderAnnotations();
        });

        saveAnnotationButton.addEventListener('click', () => {
            if (selectedAnnotation !== null) {
                annotations[selectedAnnotation].label = annotationLabelInput.value.trim();
                renderAnnotations();
                deselectAnnotation();
            }
        });

        deleteAnnotationButton.addEventListener('click', () => {
            if (selectedAnnotation !== null) {
                annotations.splice(selectedAnnotation, 1);
                renderAnnotations();
                deselectAnnotation();
            }
        });

        annotationLabelInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter') {
                saveAnnotationButton.click();
            }
        });

        // Sidebar navigation
        sidebarItems.forEach((item, index) => {
            item.addEventListener('click', () => {
                sidebarItems.forEach(li => li.classList.remove('active'));
                sidebarContents.forEach(content => content.classList.add('hidden'));
                item.classList.add('active');
                sidebarContents[index].classList.remove('hidden');
            });
        });

        // Zoom functionality
        function applyZoom() {
            annotationImage.style.transform = `scale(${zoomLevel})`;
        }

        zoomInButton.addEventListener('click', () => {
            zoomLevel += zoomStep;
            zoomLevelDisplay.textContent = `${Math.round(zoomLevel * 100)}%`;
            applyZoom();
        });

        zoomOutButton.addEventListener('click', () => {
            if (zoomLevel > zoomStep) {
                zoomLevel -= zoomStep;
                zoomLevelDisplay.textContent = `${Math.round(zoomLevel * 100)}%`;
                applyZoom();
            }
        });

        resetZoomButton.addEventListener('click', () => {
            zoomLevel = 1;
            zoomLevelDisplay.textContent = '100%';
            applyZoom();
        });

        // Initial setup
        displayRawData(sampleRawData);
        annotationEditor.style.display = 'none';
    </script>
</body>
</html>
""",height=1700,scrolling=True)