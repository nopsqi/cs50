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
    document.querySelector('#email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';

    document.querySelector('#compose-form').onsubmit = function(item) {
        fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                recipients: document.querySelector('#compose-recipients').value,
                subject: document.querySelector('#compose-subject').value,
                body: document.querySelector('#compose-body').value
            })
        })
        .then(response => response.json())
        .then(result => {
            if (result.hasOwnProperty("message")) {
                alert(result.message)
            }
            else
            {
                alert(result.error)
            }
        })
        .finally(() => {
            compose_email()
        })
        return false
    }
}

function load_mailbox(mailbox) {

    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    fetch(`/emails/${mailbox}`)
        let div = document.createElement("div")
        .then(data => data.json())
        .then(data => {data.forEach(item => {
            const readIndicator = "bg-light"
            div.classList.add("card", "p-2")
            if (item.read) {
                div.classList.add(readIndicator)
            }
            div.innerHTML = `
                <div class="row">
                    <div class="col-md-3 font-weight-bold">${mailbox === 'sent' ? 'To: ' + item.recipients[0] + (item.recipients.length > 0 ? '...' : '') : item.sender}</div>
                    <div class="col-md-2">${item.subject}</div>
                    <div class="col-md-5">${item.body}</div>
                    <div dlass="col-md-2 text-right">${item.timestamp}</div>
                </div>
            `
            Array.from(div.querySelector('.row').children).forEach(item => {
                item.classList.add("card-text");
                item.style.whiteSpace = 'nowrap';
                item.style.overflow = 'hidden';
                item.style.textOverflow = 'ellipsis'
            })

            const hoverIndicator = "border-dark"
            div.onmouseenter = function(item) {
                this.classList.add(hoverIndicator)
            }
            div.onmouseleave = function() {
                this.classList.remove(hoverIndicator)
            }
            div.onclick = () => load_mail(mailbox, item.id)
            document.querySelector('#emails-view').append(div);
        })})
        .catch(error => {
            console.log(error)
        });
}

function load_mail(mailbox, id) {
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#email-view').innerHTML = '';
    document.querySelector('#email-view').style.display = 'block';

    fetch(`/emails/${parseInt(id)}`)
    .then(data => data.json())
    .then(data => {
        document.querySelector('#email-view').innerHTML = `
            <div class="row">
                <div class="col-md-6">
                    <div class="font-weight-bold">${data.sender}</div>
                </div>
                <div class="col-md-6">
                    <div id="timestamp" class="d-flex justify-content-end align-items-center">
                        <div class="text-muted">${data.timestamp}</div>
                    </div>
                </div>
            </div>
            <div>to ${mailbox == 'sent' ? data.recipients[0] + (data.recipients.length > 1 ? '...' : '') : 'me'} <span class="badge badge-secondary">v</span></div>
            <div style="display: none" id="recipients">recipients: ${data.recipients.join(", ")}</div>
            <h3 class="mt-3">${data.subject}</h3>
            <p class="mt-3">${data.body}</p>
        `
        const div = document.createElement('div')
        recipients = document.querySelector('#recipients')
        document.querySelector('#email-view span').onclick = function() {
            if (recipients.style.display === 'none') {
                this.innerHTML = 'A';
                recipients.style.display = 'block';
            }
            else
            {
                this.innerHTML = 'V';
                recipients.style.display = 'none';
            }
        }
        if (mailbox !== 'sent') {
            const replyButton = document.createElement('button')
            replyButton.classList.add('btn', 'ml-3')
            replyButton.innerHTML = 'Archived'
            if (data.archived) {
                replyButton.classList.add('btn-secondary')
            }
            else
            {
                replyButton.classList.add('btn-primary')
            }
            document.querySelector('#timestamp').append(replyButton)
            replyButton.onclick = function() {
                if (replyButton.classList.contains('btn-secondary')) {
                    replyButton.classList.remove('btn-secondary')
                    replyButton.classList.add('btn-primary')
                }
                else
                {
                    replyButton.classList.remove('btn-primary')
                    replyButton.classList.add('btn-secondary')
                }
                updateEmail(id, {archived: !data.archived})
            }
        }
        updateEmail(id, {read: true})
    })
}

function updateEmail(id, body) {
    fetch(`emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify(body)
    })
}
