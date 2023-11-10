const NewPost = () => {
    const [state, setState] = React.useState({value: ""})

    return (
        <form className="mt-3 text-right">
            <textarea type="text" className="form-control" onChange={(e) => {setState({value: e.target.value})}} value={state.value}></textarea>
            <button className="mt-2 btn btn-primary">Post</button>
        </form>
    )
}

ReactDOM.render(<NewPost />, document.getElementById('new-post'))
