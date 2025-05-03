// Coding Dojo - Python Bootcamp Jan 2025
// Final project
// Wavely - Scripts Java

document.addEventListener('DOMContentLoaded', function () {
    // Aplicar tema guardado al cargar la página
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.classList.toggle('dark-theme', savedTheme === 'dark');
    
    // Manejar clics en los enlaces del sidebar
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function () {
            navLinks.forEach(l => {
                l.classList.remove('active');
                l.classList.add('text-white');
            });
            this.classList.add('active');
            this.classList.remove('text-white');
        });
    });

    // Inicializar los botones de favoritos
    const favoriteButtons = document.querySelectorAll('.action-btn.favorite');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', () => handleFavorite(button));
    });

    // Obtener referencias a los elementos de configuración
    const profileForm = document.querySelector('#profileForm');
    const themeRadios = document.querySelectorAll('input[name="theme"]');
    const notificationSwitches = document.querySelectorAll('.form-check-input[type="checkbox"]');
    const privacySelect = document.querySelector('#visibility');
    const passwordForm = document.querySelector('#securityForm');

    // Cargar configuraciones guardadas
    loadSavedSettings();

    // Event listeners para cambios en la configuración
    if (profileForm) {
        profileForm.addEventListener('submit', function(e) {
            e.preventDefault();
            saveProfileChanges();
        });
    }

    themeRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            applyTheme(this.id === 'darkTheme' ? 'dark' : 'light');
        });
    });

    notificationSwitches.forEach(switch_ => {
        switch_.addEventListener('change', function() {
            saveNotificationSettings();
        });
    });

    if (privacySelect) {
        privacySelect.addEventListener('change', function() {
            savePrivacySettings();
        });
    }

    if (passwordForm) {
        passwordForm.addEventListener('submit', function(e) {
            e.preventDefault();
            changePassword();
        });
    }
});

//
// Funciones para favoritos & likes

// Función para manejar los favoritos
function handleFavorite(button) {
    if (button.classList.contains('active')) {
        button.classList.remove('active');
        // Aquí puedes agregar la lógica para eliminar de favoritos
    } else {
        button.classList.add('active');
        // Aquí puedes agregar la lógica para agregar a favoritos
    }
}

// Función para atualizar contadores
function updateCounter(button, action) {
    const counter = button.querySelector('.counter');
    let count = parseInt(counter.textContent);
    counter.textContent = count + 1;
    button.classList.add('active');
    
    // Cambiar el color del ícono si es el botón de favoritos
    if (action === 'favorite') {
        const icon = button.querySelector('i');
        icon.style.color = '#ffd700';
    }
}

//
// Funciones para la página de configuración

function loadSavedSettings() {
    // Cargar tema
    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);
    document.querySelector(`#${savedTheme}Theme`).checked = true;

    // Cargar notificaciones
    const notifications = JSON.parse(localStorage.getItem('notifications') || '{}');
    Object.keys(notifications).forEach(id => {
        const element = document.querySelector(`#${id}`);
        if (element) element.checked = notifications[id];
    });

    // Cargar configuración de privacidad
    const privacy = localStorage.getItem('privacy');
    if (privacy && privacySelect) {
        privacySelect.value = privacy;
    }
}

function applyTheme(theme) {
    const body = document.body;
    if (theme === 'dark') {
        body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark');
    } else {
        body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light');
    }
}

function saveProfileChanges() {
    const username = document.querySelector('#username').value;
    const email = document.querySelector('#email').value;

    fetch('/update_profile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            toastr.success('Perfil actualizado correctamente');
        } else {
            toastr.error('Error al actualizar el perfil');
        }
    })
    .catch(error => {
        toastr.error('Error de conexión');
    });
}

function saveNotificationSettings() {
    const notifications = {};
    document.querySelectorAll('.form-check-input[type="checkbox"]').forEach(checkbox => {
        notifications[checkbox.id] = checkbox.checked;
    });
    localStorage.setItem('notifications', JSON.stringify(notifications));
    toastr.success('Configuración de notificaciones guardada');
}

function savePrivacySettings() {
    const privacy = document.querySelector('#visibility').value;
    localStorage.setItem('privacy', privacy);
    toastr.success('Configuración de privacidad guardada');
}


// Roberto's comment: creo que debemos usar otra manera de utualizar password

function changePassword() {
    const currentPassword = document.querySelector('#currentPassword').value;
    const newPassword = document.querySelector('#newPassword').value;
    const confirmPassword = document.querySelector('#confirmPassword').value;

    if (newPassword !== confirmPassword) {
        toastr.error('Las contraseñas no coinciden');
        return;
    }

    fetch('/change_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            currentPassword,
            newPassword
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            toastr.success('Contraseña actualizada correctamente');
            document.querySelector('#passwordForm').reset();
        } else {
            toastr.error(data.message || 'Error al actualizar la contraseña');
        }
    })
    .catch(error => {
        toastr.error('Error de conexión');
    });
}