const NewPost = () => {
    return (
        <form className="mt-3 text-right">
            <textarea className="form-control"></textarea>
            <button className="mt-2 btn btn-primary">Post</button>
        </form>
    )
}

ReactDOM.render(<NewPost />, document.getElementById('new-post'))
