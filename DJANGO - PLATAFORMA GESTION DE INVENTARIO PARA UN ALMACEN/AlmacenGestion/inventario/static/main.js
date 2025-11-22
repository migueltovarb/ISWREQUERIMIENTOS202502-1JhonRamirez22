// Cerrar mensajes automáticamente
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        const closeBtn = alert.querySelector('.close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                alert.style.display = 'none';
            });
        }
        
        // Auto-close after 5 seconds
        setTimeout(() => {
            if (alert.style.display !== 'none') {
                alert.style.animation = 'slideIn 0.3s ease reverse';
                setTimeout(() => {
                    alert.style.display = 'none';
                }, 300);
            }
        }, 5000);
    });
    
    // Confirmar eliminación
    const deleteButtons = document.querySelectorAll('a[href*="/eliminar/"]');
    deleteButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!confirm('¿Está seguro de que desea eliminar este elemento?')) {
                e.preventDefault();
            }
        });
    });
});

// Validación de formularios
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('error');
            isValid = false;
        } else {
            input.classList.remove('error');
        }
    });
    
    return isValid;
}

// Buscar productos
function searchProducts(query) {
    const form = document.querySelector('.search-form');
    if (form) {
        form.submit();
    }
}

// Copiar código de barras
function copyBarcode(codigo) {
    navigator.clipboard.writeText(codigo).then(() => {
        alert('Código copiado al portapapeles');
    });
}

// Filtrar alertas
function filterAlerts(filtro) {
    window.location.href = '?filtro=' + filtro;
}
