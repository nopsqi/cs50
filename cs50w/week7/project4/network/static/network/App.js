const allPostsNav = document.getElementById('all-posts-nav')
const followingNav = document.getElementById('following-nav')

if (document.location.pathname === '/') {
    allPostsNav.style.display = 'block'
    followingNav.style.display = 'block'
    allPostsNav.classList.add('active')
} else {
    allPostsNav.style.display = 'none'
    followingNav.style.display = 'none'
    allPostsNav.classList.remove('active')
}

const App = () => {
    const [state, setState] = React.useState({
        myUsername: document.getElementById('App').dataset.myUsername,
        api: new URL(document.getElementById('App').dataset.api, document.location.origin),
        fetch: true,
        loading: true,
        newPostValue: "",
        editPostValue: ""
    })

    React.useEffect(() => {
        setState({
            ...state,
            loading: true
        })

        fetchPosts(state.api)
    }, [state.api, state.fetch])

    allPostsNav.onclick = (e) => {
        e.preventDefault()
        e.target.classList.add('active')
        followingNav.classList.remove('active')
        const api = new URL(state.api.href)
        api.searchParams.delete('following')
        setState({
            ...state,
            api: api
        })
    }

    followingNav.onclick = (e) => {
        e.preventDefault()
        e.target.classList.add('active')
        allPostsNav.classList.remove('active')
        const api = new URL(state.api.href)
        api.searchParams.set('following', true)
        setState({
            ...state,
            api:api
        })
    }

    const fetchPosts = (api) => {
        fetch(api)
            .then(response => {
                if (response.status === 200) {
                    response.json()
                        .then(result => {
                            setState({
                                ...state,
                                loading: false,
                                ...result,
                            })
                        })
                }
                else if (response.status === 404) {
                    response.json()
                        .then(result => {
                            const api = new URL(state.api.href)
                            api.searchParams.set('page', result.pages)
                            setState({
                                ...state,
                                api: api
                            })
                        })
                }
            })
    }

    const addPost = (e) => {
        e.preventDefault()
        fetch('/api/post', {
            method: 'POST',
            body: JSON.stringify({
                content: state.newPostValue
            })
        })
            .then(response => {
                if (response.status === 200) {
                    setState({
                        ...state,
                        fetch: !state.fetch
                    })
                }
            })
    }

    const getParamsToState = (e, obj) => {
        setState({
            ...state,
            ...obj
        })
    }

    const deletePost = (e) => {
        e.preventDefault()
        fetch('/api/post', {
            method: 'DELETE',
            body: JSON.stringify({
                id: state.deleteId
            })
        })
            .then(response => {
                if (response.status == 200) {
                    response.json()
                        .then(result => {
                            setState({
                                ...state,
                                fetch: !state.fetch
                            })
                        })
                }
            })
    }

    const editPost = (e) => {
        e.preventDefault()
        fetch('/api/post', {
            method: 'PUT',
            body: JSON.stringify({
                id: state.editId,
                content: state.editPostValue
            })
        })
        .then(response => {
            if (response.status === 200) {
                setState({
                    ...state,
                    fetch: !state.fetch
                })
            }
        })
    }

    const goToPage = (e) => {
        e.preventDefault()
        const api = new URL(state.api.href)
        if (e.target.innerHTML == "Next") {
            api.searchParams.set('page', Math.min(state.page + 1, state.pages))
        } else {
            api.searchParams.set('page', Math.max(state.page - 1, 1))
        }
        setState({
            ...state,
            api: api
        })
    }

    const newPost = ['', state.myUsername].includes(document.location.pathname.slice(1))

    if (state.loading) {
        return (
            <div>
            {
                newPost
                ?
                <NewPost onSubmit={addPost} onChange={getParamsToState} />
                :
                ''
            }
            </div>
        )
    }

    return (
        <div>
            <DeleteConfirmationModal deletePost={deletePost} />
            <EditModal editPost={editPost} onChange={getParamsToState} value={state.editPostValue}/>
            {
                newPost
                ?
                <NewPost onSubmit={addPost} onChange={getParamsToState} />
                :
                ''
            }
            <Posts myUsername={state.myUsername} posts={state.posts} deleteClick={getParamsToState} editClick={getParamsToState} />
            <Paginator pages={state.pages} page={state.page} onClick={goToPage} />
        </div>
    )
}

const NewPost = (props) => {
    return (
        <form className="mt-3 text-right" onSubmit={props.onSubmit}>
            <textarea type="text" name="post" className="form-control" value={props.value} onChange={(e) => props.onChange(e, {
                newPostValue: e.target.value
            })}></textarea>
            <button type="submit" className="mt-2 btn btn-primary">Post</button>
        </form>
    )
}

const Posts = (props) => {
    return (
        <div>
            {props.posts.map((post, index) => (
                <Post myUsername={props.myUsername} key={index} {...post} deleteClick={props.deleteClick} editClick={props.editClick} />
            ))}
        </div>
    )
}

const Post = (props) => {
    const [state, setState] = React.useState({
        like: props.like,
        likes_length: props.likes.length
    })

    const heart = {
        before: (
            '<svg syle="fill: #1a2a47" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M225.8 468.2l-2.5-2.3L48.1 303.2C17.4 274.7 0 234.7 0 192.8v-3.3c0-70.4 50-130.8 119.2-144C158.6 37.9 198.9 47 231 69.6c9 6.4 17.4 13.8 25 22.3c4.2-4.8 8.7-9.2 13.5-13.3c3.7-3.2 7.5-6.2 11.5-9c0 0 0 0 0 0C313.1 47 353.4 37.9 392.8 45.4C462 58.6 512 119.1 512 189.5v3.3c0 41.9-17.4 81.9-48.1 110.4L288.7 465.9l-2.5 2.3c-8.2 7.6-19 11.9-30.2 11.9s-22-4.2-30.2-11.9zM239.1 145c-.4-.3-.7-.7-1-1.1l-17.8-20c0 0-.1-.1-.1-.1c0 0 0 0 0 0c-23.1-25.9-58-37.7-92-31.2C81.6 101.5 48 142.1 48 189.5v3.3c0 28.5 11.9 55.8 32.8 75.2L256 430.7 431.2 268c20.9-19.4 32.8-46.7 32.8-75.2v-3.3c0-47.3-33.6-88-80.1-96.9c-34-6.5-69 5.4-92 31.2c0 0 0 0-.1 .1s0 0-.1 .1l-17.8 20c-.3 .4-.7 .7-1 1.1c-4.5 4.5-10.6 7-16.9 7s-12.4-2.5-16.9-7z"/></svg>'
        ),
        after: (
            '<svg style="fill: #fd3a3a" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M47.6 300.4L228.3 469.1c7.5 7 17.4 10.9 27.7 10.9s20.2-3.9 27.7-10.9L464.4 300.4c30.4-28.3 47.6-68 47.6-109.5v-5.8c0-69.9-50.5-129.5-119.4-141C347 36.5 300.6 51.4 268 84L256 96 244 84c-32.6-32.6-79-47.5-124.6-39.9C50.5 55.6 0 115.2 0 185.1v5.8c0 41.5 17.2 81.2 47.6 109.5z"/></svg>'
        )
    }

    const switchLike = (e) => {
        e.preventDefault()
        fetch('/api/post', {
            method: 'PUT',
            body: JSON.stringify({
                id: props.id,
                like: state.like
            })
        })
            .then(response => {
                if (response.status === 200) {
                    response.json()
                    .then(result => {
                        setState({
                            ...state,
                            like: result.like,
                            likes_length: result.likes.length
                        })
                    })
                }
            })
    }

    return (
        <div className="card mt-2">
            <div className="card-body">
                <div className="row">
                    <div className="col-md-4">
                        <div className="d-flex">
                            <a href={`${document.location.origin}/${props.username}`} className="text-card">{props.username}</a>
                            <div className="text-card text-muted ml-1">{props.modified}</div>
                        </div>
                    </div>
                    <div className="col"></div>
                    <div className="col-md-1 text-right">
                        {
                            props.myUsername === props.username
                            ?
                            <Dropdown id={props.id} content={props.content} deleteClick={props.deleteClick} editClick={props.editClick} />
                            :
                            ''
                        }
                    </div>
                </div>
                <div className="text-card">{props.content}</div>
                <div className="d-flex">
                    <div className="d-flex align-items-center">
                        <a href="" className="text-card d-flex" onClick={switchLike} dangerouslySetInnerHTML={{ __html: state.like ? heart.after : heart.before }} />
                        <div className="text-card ml-2">{state.likes_length}</div>
                    </div>
                </div>
            </div>
        </div>
    )
}

const Dropdown = (props) => {
    const icon = (
        '<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 128 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M64 360a56 56 0 1 0 0 112 56 56 0 1 0 0-112zm0-160a56 56 0 1 0 0 112 56 56 0 1 0 0-112zM120 96A56 56 0 1 0 8 96a56 56 0 1 0 112 0z"/></svg>'
    )

    return (
        <div className="dropdown ml-3">
            <a href="" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" dangerouslySetInnerHTML={{ __html: icon }} />
            <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a className="dropdown-item" href="" onClick={(e) => props.deleteClick(e, {
                    deleteId: props.id,
                })} data-toggle="modal" data-target="#deleteConfirmationModal">Delete</a>
                <a className="dropdown-item" href="" onClick={(e) => props.editClick(e, {
                    editId: props.id,
                    editPostValue: props.content
                })} data-toggle="modal" data-target="#editModal">Edit</a>
            </div>
        </div>
    )
}

const Paginator = (props) => {
    return (
        <div>
            <nav className="mt-2" aria-label="Post navigaioon">
                <ul className="pagination justify-content-end">
                    <li className={`page-item ${props.page <= 1? 'disabled' : ''}`}>
                        <a className="page-link" href="" onClick={props.onClick}>Previous</a>
                    </li>
                    <li className={`page-item ${props.page >= props.pages? 'disabled' : ''}`}>
                        <a className="page-link" href="" onClick={props.onClick}>Next</a>
                    </li>
                </ul>
            </nav>
        </div>
    )
}

const DeleteConfirmationModal = (props) => {
    return (
        <div className="modal fade" id="deleteConfirmationModal" tabindex="-1" role="dialog" aria-labelledby="deleteConfirmationModal" aria-hidden="true">
            <div className="modal-dialog" role="document">
                <div className="modal-content">
                    <div className="modal-header">
                        <h5 className="modal-title" id="exampleModalLabel">Delete Confirmation</h5>
                        <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div className="modal-body">
                        Are you sure you want to delete the post?
                    </div>
                    <div className="modal-footer">
                        <button type="button" className="btn btn-secondary" data-dismiss="modal">Close</button>
                        <button type="button" className="btn btn-danger" onClick={props.deletePost} data-toggle="modal" data-target="#deleteConfirmationModal">Delete</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

const EditModal = (props) => {
    return (
        <div class="modal fade" id="editModal" tabindex="-1" role="dialog" aria-labelledby="editModal" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Edit Post</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="form-group">
                                <textarea class="form-control" name="post" onChange={(e) => props.onChange(e, {
                                    editPostValue: e.target.value
                                })} value={props.value} rows="5"></textarea>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        <button type="button" onClick={props.editPost} class="btn btn-primary" data-toggle="modal" data-target="#editModal">Edit</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))
