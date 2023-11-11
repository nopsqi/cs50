const App = () => {
    const [state, setState] = React.useState({
        api: new URL(document.getElementById('App').dataset.api, document.location.origin),
        fetch: true,
        loading: true,
    })

    React.useEffect(() => {
        setState({
            ...state,
            loading: true
        })

        fetchPosts(state.api)
    }, [state.api, state.fetch])

    const fetchPosts = (api) => {
        fetch(api)
        .then(response => {
            console.log("fetching", state.api.href)
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
                    const api = state.api
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
        setState({
            ...state,
            posts: [...state.posts, {id: 17}]
        })
    }

    const deletePost = (e) => {
        fetch('/api/post', {
            method: 'DELETE',
            body: JSON.stringify({
                id: parseInt(e.target.parentElement.childNodes[1].innerHTML)
            })
        })
        .then(response => {
            if (response.status == 200) {
                response.json()
                .then(result => console.log(result))
            }
        })
    }

    const goToPage = (e) => {
        e.preventDefault()
        const api = new URL(state.api.href)
        api.searchParams.set('page', parseInt(e.target.innerHTML))
        setState({
            ...state,
            api: api
        })
    }

    if (state.loading) {
        return (<div></div>)
    }

    return (
        <div>
            <h1>APP HOLDER</h1>
            <h2>{state.api.href}</h2>
            <NewPost onClick={addPost} />
            <Posts posts={state.posts} onClick={deletePost} />
            <Paginator pages={state.pages} page={state.page} onClick={goToPage} />
        </div>
    )
}

const NewPost = (props) => {
    return (
        <div>
            <h2>NEW POST HOLDER</h2>
            <button onClick={props.onClick}>Add Post</button>
        </div>
    )
}

const Posts = (props) => {
    return (
        <div>
            <h2>POSTS HOLDER</h2>
            {props.posts.map((post, index) => (
                <Post key={index} {...post} onClick={props.onClick}/>
            ))}
        </div>
    )
}

const Post = (props) => {
    return (
        <div>
            <h3>POST HOLDER</h3>
            <div>{props.id}</div>
            <button onClick={props.onClick}>Delete</button>
        </div>
    )
}

const Paginator = (props) => {
    return (
        <div>
            <h2>PAGINATOR HOLDER</h2>
            <nav className="mt-3" aria-label="Post navigaioon">
                <ul className="pagination justify-content-end">
                    {Array.from({length: props.pages}, (_, i) => i + 1).map((item) => (
                        <li key={item} className={`page-item ${item === props.page ? 'active' : ''}`}>
                            <a className="page-link" href="" onClick={props.onClick}>{item}</a>
                        </li>
                    ))}
                </ul>
            </nav>
        </div>
    )
}

const Modal = (props) => {
    return (
        <div class="modal fade" id="staticBackdrop" data-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="staticBackdropLabel">Modal title</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        ...
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary">Understood</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))
