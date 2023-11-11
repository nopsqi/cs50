const App = () => {
    const [state, setState] = React.useState({
        api: new URL(document.getElementById('App').dataset.api, document.location.origin),
        loading: true,
    })

    React.useEffect(() => {
        setState({
            ...state,
            loading: true
        })

        fetch(state.api)
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
    }, [state.api])

    const addPost = (e) => {
        setState({
            ...state,
            posts: [...state.posts, {id: 17}]
        })
    }

    const deletePost = (e) => {
        setState({
            ...state,
            posts: state.posts.filter((item, index) => item.id !== parseInt(e.target.parentElement.childNodes[1].innerHTML))
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

ReactDOM.render(<App />, document.getElementById('App'))
