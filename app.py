from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Inicializar datos
ACTIVOS = []
PASIVOS = []
INGRESOS = []
EGRESOS = []

@app.route('/')
def index():
    return render_template('index.html')  # Página principal

@app.route('/activos', methods=['GET', 'POST'])
def gestionar_activos():
    if request.method == 'POST':
        # Capturar datos del formulario
        cuenta = request.form['cuenta']
        monto = request.form['monto']
        ACTIVOS.append([cuenta, monto])
        return redirect(url_for('gestionar_activos'))
    return render_template('activos.html', activos=ACTIVOS)

@app.route('/pasivos', methods=['GET', 'POST'])
def gestionar_pasivos():
    if request.method == 'POST':
        cuenta = request.form['cuenta']
        monto = request.form['monto']
        PASIVOS.append([cuenta, monto])
        return redirect(url_for('gestionar_pasivos'))
    return render_template('pasivos.html', pasivos=PASIVOS)

@app.route('/resultados')
def resultado():
    total_activos = sum(int(activo[1]) for activo in ACTIVOS)
    total_pasivos = sum(int(pasivo[1]) for pasivo in PASIVOS)
    patrimonio_neto = total_activos - total_pasivos
    return render_template('resultados.html', 
                           total_activos=total_activos, 
                           total_pasivos=total_pasivos, 
                           patrimonio_neto=patrimonio_neto)

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    global ACTIVOS, PASIVOS
    ACTIVOS.clear()
    PASIVOS.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
