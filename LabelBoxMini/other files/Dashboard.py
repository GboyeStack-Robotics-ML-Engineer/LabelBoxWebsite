import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="LabelBoxMini",
    page_icon="🧊",
    layout="wide"
)


def show_upload_modal():
    components.html(
        f"""
        <div id="uploadModal" class="modal" style="display: block;">
            <div class="modal-content">
            <span class="close-modal" onclick="closeModal()">×</span>
                <h2>Upload New Project</h2>
                 <p> Upload Image below: </p>
                 {st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="image_upload", on_change=handle_upload_change,label_visibility="collapsed")}
                <div id="imageDisplay">
                </div>
                <br>
                <button class="upload-button" onclick="uploadImage()"> Create Project </button>
            </div>
         </div>
         """,
         height=1000,
         scrolling=True,
    )

def handle_upload_change():
    uploaded_file = st.session_state.get('image_upload')
    if uploaded_file is not None:
        image_preview = f"""<img src="data:image/png;base64,{base64.b64encode(uploaded_file.read()).decode()}" alt="uploaded image preview" class="preview-image" />"""
        components.html(f"""
        <script>
           document.getElementById('imageDisplay').innerHTML = `{image_preview}`;
        </script>
        """, height=200)




def upload_to_database():

    uploaded_file = st.session_state.get('image_upload')
    if uploaded_file is not None:
        st.session_state.upload_complete = True
        st.success("Image Successfully uploaded to the database")
    else:
        st.warning("Please upload an image")


components.html(
    """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roboflow Clone</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" integrity="sha512-9usAa10IRO0HhonpyAIVpjrylPvoDwiPUiKdWk5t3PyolY1cOd4DSE0Ga+ri4AuTroPR5aQvXU9xC6qOPnzFeg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f8f8f8;
            overflow: hidden;
            padding: 0;
            display: flex;
        }

        .sidebar {
            width: 250px;
            background-color: #6a0dad;
            color: #fff;
            padding: 20px;
            display: flex;
            flex-direction: column;
            height: 100vh;
            border-top-right-radius: 20px;
            border-bottom-right-radius: 20px;
            transition: width 0.3s ease;
        }

         .sidebar.collapsed {
            width: 60px; /* Collapsed width */
         }

        .sidebar h1 {
            font-size: 24px;
            margin-bottom: 30px;
            font-weight: bold;
            white-space: nowrap;
        }
        .sidebar.collapsed h1 {
            font-size: 0;
             margin-bottom: 0px;
        }

        .sidebar ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .sidebar ul li {
            margin-bottom: 15px;
        }


        .sidebar ul li a {
            text-decoration: none;
            color: #fff;
            display: flex;
            align-items: center;
            padding: 10px 15px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .sidebar ul li a i {
            margin-right: 10px;
        }
         .sidebar.collapsed ul li a i {
             margin-right: 0;

         }

        .sidebar ul li a span {
            white-space: nowrap; /* Prevent text from wrapping */
             transition: opacity 0.3s ease;
        }
         .sidebar.collapsed ul li a span {
            opacity: 0; /* Hide text when collapsed */
            width: 0;
            overflow: hidden;
        }
        .sidebar ul li a:hover {
             background-color: rgba(255, 255, 255, 0.1);
        }

        .sidebar .upgrade-btn {
            background-color: #fff;
            color: #6a0dad;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: auto;
              transition: background-color 0.3s ease;
              white-space: nowrap;
        }
         .sidebar.collapsed .upgrade-btn{
           padding: 10px;

           white-space: normal;
            font-size: 0;
         }
          .sidebar .upgrade-btn:hover{
           background-color: rgba(255, 255, 255, 0.5);
        }
          .sidebar .upgrade-btn i{
               margin-right: 10px;
              transition: margin 0.3s ease;
           }
          .sidebar.collapsed .upgrade-btn i{
               margin-right: 0px;
          }
         .sidebar .upgrade-btn span{
            transition: opacity 0.3s ease;
         }
        .sidebar.collapsed .upgrade-btn span{
            opacity: 0;
             width: 0;
            overflow: hidden;
        }
         .sidebar-toggle-btn {
           position: absolute;
           top: 20px;
           right: 20px;
           background: transparent;
           border: none;
           color: white;
           font-size: 20px;
           cursor: pointer;
            z-index: 1000;
        }
         .sidebar-toggle-btn:hover{
            opacity: 0.8;
         }
         .sidebar.collapsed .sidebar-toggle-btn{
            left: 60px;
            right: auto;
         }


         .main-content {
            flex: 1;
            padding: 20px;
            display: flex;
            flex-direction: column;
            height: 100vh;
            overflow-y: auto;
         }

          .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
         }

        .top-bar h2 {
             font-size: 24px;
             margin: 0;
         }

        .top-bar .actions {
              display: flex;
             align-items: center;
         }

        .top-bar .actions button {
            padding: 8px 16px;
            margin-left: 10px;
            border-radius: 8px;
            cursor: pointer;
             border: none;
           background-color: #6a0dad;
           color: #fff;
            transition: background-color 0.3s ease;
        }
         .top-bar .actions button:hover{
              background-color: rgba(106, 13, 173, 0.8);
         }
         .search-sort {
             display: flex;
            align-items: center;
            margin-bottom: 20px;
        }

        .search-sort input {
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 8px;
            margin-right: 10px;
        }

        .search-sort select {
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 8px;
             cursor: pointer;
        }

        .project-grid {
             display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }

        .project-card {
           background-color: #fff;
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
             transition: transform 0.3s ease, box-shadow 0.3s ease;
         }
        .project-card:hover {
             transform: translateY(-5px);
             box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

         .project-card img {
           width: 100%;
            height: auto;
            border-radius: 10px;
            margin-bottom: 10px;
        }

        .project-card h3 {
            font-size: 18px;
            margin: 0;
            margin-bottom: 5px;
            font-weight: bold;
            color: #6a0dad;
        }

        .project-card p {
             font-size: 14px;
            color: #777;
           margin: 0;
         }

         .project-card .details {
          flex: 1; /* Allow details to take up remaining vertical space */
          display: flex;
           flex-direction: column;
          justify-content: space-between;
         }
         .project-card .menu {
            position: relative;
            align-self: flex-start;
           margin-left: auto;
           cursor: pointer;

        }

        .project-card .menu-dropdown {
            position: absolute;
            top: 100%;
            right: 0;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 4px;
            display: none;
            z-index: 100;

        }

         .project-card .menu-dropdown.active {
              display: block;
         }

        .project-card .menu-dropdown button{
            display: block;
            padding: 8px 15px;
             background-color: transparent;
            border: none;
            width: 100%;
            text-align: left;
            cursor: pointer;
              transition: background-color 0.3s ease;
        }
        .project-card .menu-dropdown button:hover{
             background-color: rgba(106, 13, 173, 0.1);
        }

         .modal {
             position: fixed;
            z-index: 1000;
            left: 0;
             top: 0;
            width: 100%;
             height: 100%;
            overflow: auto;
             background-color: rgba(0, 0, 0, 0.4);
             display: none;
            
        }

        .modal-content {
            background-color: #fefefe;
             margin: 15% auto;
            padding: 20px;
             border: 1px solid #888;
            width: 50%;
             border-radius: 10px;
           position: relative;
        }

        .close-modal{
            color: #aaa;
           float: right;
             font-size: 28px;
             font-weight: bold;
            cursor: pointer;
          position: absolute;
           top: 10px;
          right: 20px;
       }

        .close-modal:hover{
            color: black;
        }

        .upload-button {
             background-color: #6a0dad;
             color: white;
             padding: 10px 20px;
              border: none;
            border-radius: 5px;
            cursor: pointer;
             transition: background-color 0.3s ease;
            margin-top: 10px;
        }
         .upload-button:hover {
             background-color: rgba(106, 13, 173, 0.8);
        }
        .preview-image{
            max-width: 100%;
            max-height: 200px;
           border-radius: 10px;
        }
        /* Style adjustments to make the sidebar responsive on small screens */
        @media (max-width: 768px) {
             body {
               flex-direction: column; /* Stack sidebar and main content vertically on small screens */
            }

            .sidebar {
                width: 100%;
                height: auto;
                  border-radius: 0;
            }

           .main-content {
                 height: auto;
            }
         }
    </style>
</head>
<body>
     <aside class="sidebar" id="sidebar">
       <button class="sidebar-toggle-btn" onclick="toggleSidebar()"> <i class="fas fa-bars"></i></button>
        <h1>Roboflow</h1>
        <ul>
            <li><a href="#projects"><i class="fas fa-folder"></i><span>Projects</span></a></li>
            <li><a href="#workflows"><i class="fas fa-cogs"></i><span>Workflows</span></a></li>
            <li><a href="#monitoring"><i class="fas fa-chart-line"></i><span>Monitoring</span></a></li>
             <li><a href="#deployments"><i class="fas fa-rocket"></i><span>Deployments</span></a></li>
            <li><a href="#notifications"><i class="fas fa-bell"></i><span>Notifications</span></a></li>
            <li><a href="#settings"><i class="fas fa-cog"></i><span>Settings</span></a></li>
            <li><a href="#universe"><i class="fas fa-globe"></i><span>Universe</span></a></li>
            <li><a href="#documentation"><i class="fas fa-book"></i><span>Documentation</span></a></li>
            <li><a href="#help"><i class="fas fa-question-circle"></i><span>Help</span></a></li>
        </ul>
         <button class="upgrade-btn"> <i class="fas fa-arrow-up"></i> <span>Upgrade</span></button>
     </aside>

    <main class="main-content">
          <div class="top-bar">
            <h2>Dashboard - Projects</h2>
            <div class="actions">
                 <button>B +1</button>
                  <button>Invite Members</button>
                  <button onclick="openUploadModal()">+ New Project</button>
            </div>
        </div>
        <div class="search-sort">
            <input type="text" placeholder="Search projects">
            <select>
                <option>Sort: Date Edited</option>
                <option>Sort: Name</option>
                 <option>Sort: Images</option>
            </select>
        </div>
       <div class="project-grid">
            <div class="project-card">
                 <img src="https://transform.roboflow.com/sEDL0vDrUybihIMyLuXTVjK67uE2/6f41fb5d4c4f99c708d3f39308e453d2/thumb.jpg" alt="Project 1">
                <div class="details">
                    <div>
                        <h3>Football Analytics with Open...</h3>
                        <p>Edited 3 months ago</p>
                        <p>Private • 184 Images • 1 Models</p>
                    </div>
                    <div class="menu" onclick="toggleMenu(this)">
                      ⋮
                      <div class="menu-dropdown">
                            <button onclick="showAlert('Edit Clicked')">Edit</button>
                           <button onclick="showAlert('Delete Clicked')">Delete</button>
                     </div>
                   </div>
                </div>
           </div>

            <div class="project-card">
                <img src="https://transform.roboflow.com/sEDL0vDrUybihIMyLuXTVjK67uE2/6f41fb5d4c4f99c708d3f39308e453d2/thumb.jpg" alt="Project 2">
                <div class="details">
                      <div>
                        <h3>Car Detection</h3>
                        <p>Edited 3 months ago</p>
                        <p>Private • 716 Images • 0 Models</p>
                     </div>
                   <div class="menu" onclick="toggleMenu(this)">
                      ⋮
                      <div class="menu-dropdown">
                            <button onclick="showAlert('Edit Clicked')">Edit</button>
                           <button onclick="showAlert('Delete Clicked')">Delete</button>
                     </div>
                   </div>
                </div>
            </div>

            <div class="project-card">
                 <img src="https://transform.roboflow.com/sEDL0vDrUybihIMyLuXTVjK67uE2/6f41fb5d4c4f99c708d3f39308e453d2/thumb.jpg" alt="Project 3">
                <div class="details">
                    <div>
                           <h3>Hard Hat Sample</h3>
                           <p>Edited 2 years ago</p>
                            <p>Private • 100 Images • 1 Models</p>
                    </div>
                      <div class="menu" onclick="toggleMenu(this)">
                      ⋮
                      <div class="menu-dropdown">
                            <button onclick="showAlert('Edit Clicked')">Edit</button>
                           <button onclick="showAlert('Delete Clicked')">Delete</button>
                     </div>
                   </div>
                </div>
            </div>
              <div class="project-card">
                 <img src="https://transform.roboflow.com/sEDL0vDrUybihIMyLuXTVjK67uE2/6f41fb5d4c4f99c708d3f39308e453d2/thumb.jpg" alt="Project 1">
                <div class="details">
                    <div>
                        <h3>Football Analytics with Open...</h3>
                        <p>Edited 3 months ago</p>
                        <p>Private • 184 Images • 1 Models</p>
                    </div>
                    <div class="menu" onclick="toggleMenu(this)">
                      ⋮
                      <div class="menu-dropdown">
                            <button onclick="showAlert('Edit Clicked')">Edit</button>
                           <button onclick="showAlert('Delete Clicked')">Delete</button>
                     </div>
                   </div>
                </div>
           </div>

            <div class="project-card">
                <img src="https://transform.roboflow.com/sEDL0vDrUybihIMyLuXTVjK67uE2/6f41fb5d4c4f99c708d3f39308e453d2/thumb.jpg" alt="Project 2">
                <div class="details">
                      <div>
                        <h3>Car Detection</h3>
                        <p>Edited 3 months ago</p>
                        <p>Private • 716 Images • 0 Models</p>
                     </div>
                   <div class="menu" onclick="toggleMenu(this)">
                      ⋮
                      <div class="menu-dropdown">
                            <button onclick="showAlert('Edit Clicked')">Edit</button>
                           <button onclick="showAlert('Delete Clicked')">Delete</button>
                     </div>
                   </div>
                </div>
            </div>

            <div class="project-card">
                 <img src="https://transform.roboflow.com/sEDL0vDrUybihIMyLuXTVjK67uE2/6f41fb5d4c4f99c708d3f39308e453d2/thumb.jpg" alt="Project 3">
                <div class="details">
                    <div>
                           <h3>Hard Hat Sample</h3>
                           <p>Edited 2 years ago</p>
                            <p>Private • 100 Images • 1 Models</p>
                    </div>
                      <div class="menu" onclick="toggleMenu(this)">
                      ⋮
                      <div class="menu-dropdown">
                            <button onclick="showAlert('Edit Clicked')">Edit</button>
                           <button onclick="showAlert('Delete Clicked')">Delete</button>
                     </div>
                   </div>
                </div>
            </div>
        </div>
    </main>
  <script>
   function showAlert(message) {
            alert(message);
        }
   function toggleMenu(menu) {
            const dropdown = menu.querySelector('.menu-dropdown');
            dropdown.classList.toggle('active');
        }
    function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
             sidebar.classList.toggle('collapsed');
    }

     function openUploadModal() {
            const modal = document.getElementById('uploadModal');
            modal.style.display = 'block';
        }

        function closeModal() {
             const modal = document.getElementById('uploadModal');
             modal.style.display = 'none';
        }
       function uploadImage(){
           parent.window.dispatchEvent(new CustomEvent('uploadImageFromJs'));

        closeModal();
       }

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.menu')) {
            document.querySelectorAll('.menu-dropdown.active').forEach(dropdown => {
              dropdown.classList.remove('active');
            });
        }
    });

   </script>
</body>
</html>
""",height=1700,scrolling=True)

