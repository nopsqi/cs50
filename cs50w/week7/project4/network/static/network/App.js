const App = () => {
    const [state, setState] = React.useState({
        api: new URL(document.getElementById('App').dataset.api, document.location.origin)
    })

    React.useEffect(() => {
        fetch(`${state.api.pathname}/${state.api.search}`)
    }, [])

    state.api.searchParams.append('page', 1)

    const changeAPI = () => {
        let page = parseInt(state.api.searchParams.get('page')) + 1
        const api = new URL(state.api.href)
        api.searchParams.set('page', page)
        console.log("page", page)
        setState({
            ...state,
            api: api
        })
        // state.api.searchParams.set('page', page)
        console.log(api.href)
    }

    return (
        <div>
            <h1>{state.api.href}</h1>
            <button onClick={changeAPI}>SET</button>
            <NewPost />
            <Posts />
            <Paginator />
        </div>
    )
}

const NewPost = (props) => {
    return (
        <div>
            <h1>NEW POST HOLDER</h1>
        </div>
    )
}

const Posts = () => {
    return (
        <div>
            <h1>POSTS HOLDER</h1>
        </div>
    )
}

const Paginator = () => {
    return (
        <div>
            <h1>PAGINATOR HOLDER</h1>
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))
