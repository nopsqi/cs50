const HOST = window.location.host

document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);

    // By default, load the inbox
    load_mailbox('inbox');
});

function compose_email() {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    fetch(`/emails/${mailbox}`)
        .then(data => data.json())
        .then(data => {data.forEach(item => {
            const div = document.createElement("div")
            const readIndicator = "bg-light"
            div.classList.add("card", "p-2")
            if (item.read) {
                div.classList.add(readIndicator)
            }
            div.innerHTML = `
                <div class="row">
                    <div class="col-md-3 font-weight-bold">${item.sender}</div>
                    <div class="col-md-2">${item.subject.slice(0, 20)}</div>
                    <div class="col-md-5">${item.body.slice(0, 50)}...</div>
                    <div dlass="col-md-2 text-right">${item.timestamp}</div>
                </div>
            `
            Array.from(div.querySelector('.row').children).forEach(item => {
                item.classList.add("card-text", "overflow-auto")
            })
            const hoverIndicator = "border-dark"
            div.onmouseenter = function(item) {
                this.classList.add(hoverIndicator)
            }
            div.onmouseleave = function() {
                this.classList.remove(hoverIndicator)
            }
            div.onclick = () => load_mail(item.id)
            document.querySelector('#emails-view').append(div);
        })})
        .catch(error => {
            console.log(error)
        });
}

function load_mail(id) {
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#email-view').style.display = 'block';

    fetch(`/emails/${parseInt(id)}`)
    .then(data => data.json())
    .then(data => {
        document.querySelector('#email-view').innerHTML = `
            <div class="d-flex justify-content-between">
                <div class="font-weight-bold">${data.sender}</div>
                <div>${data.timestamp}</div>
            </div>
            <div>${data.}</div>
            <h3>${data.subject}</h3>
        `
    })
}
