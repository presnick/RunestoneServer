
def index():
    full_url = URL(args=request.args, vars=request.get_vars, host=True)
    return {'url': full_url}