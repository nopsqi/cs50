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
            if (response.status == 200) {
                response.json()
                .then(result => {
                    setState({
                        ...state,
                        loading: false,
                        ...result,
                    })
                })
            }
        })
    }, [])

    console.log(state)

    const addPost = (e) => {
        setState({
            ...state,
            posts: [...state.posts, {}]
        })
    }

    const deletePost = (e) => {
        setState
    }

    if (state.loading) {
        return (<div></div>)
    }

    return (
        <div>
            <h1>APP HOLDER</h1>
            <NewPost onClick={addPost} />
            <Posts posts={state.posts}/>
            <Paginator />
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
            {props.posts.map((item, index) => (
                <Post />
            ))}
        </div>
    )
}

const Post = (props) => {
    return (
        <div>
            <h3>POST HOLDER</h3>
        </div>
    )
}

const Paginator = () => {
    return (
        <div>
            <h2>PAGINATOR HOLDER</h2>
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))
