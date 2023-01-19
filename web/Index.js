document.getElementById('bt').addEventListener('click', async()=>{
    await eel.python_connector(document.getElementById('input').value);
})

document.getElementById('button').addEventListener('click', async()=>{
    await eel.python_connector1(document.getElementById('input').value);
})