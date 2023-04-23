import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout';
import {Head} from '@inertiajs/react';

export default function Create(props) {

    const auth = props.auth, list = props.list;
    // console.log(list.data);
    return (
        <AuthenticatedLayout
            user={auth.user}
            header={<h2 className="font-semibold text-xl text-gray-800 leading-tight">Dashboard</h2>}
        >
            <Head title="Dashboard"/>

            <div className="py-12">
                <div className="max-w-7xl mx-auto sm:px-6 lg:px-8">
                    <div className="bg-white overflow-hidden shadow-sm sm:rounded-lg">
                        <div className="p-6 text-gray-900">Create!!!</div>
                        <form className="p-4 flex space-x-4 justify-center items-center" action="/" method="post">
                            <label htmlFor="message">Laravel Question:</label>
                            <input id="message" type="text" name="message" autoComplete="off"
                                   className="border rounded-md  p-2 flex-1"/>
                            <a className="bg-gray-800 text-white p-2 rounded-md" href="/reset">Reset Conversation</a>
                        </form>
                    </div>
                </div>
            </div>
            <div className="py-12">
                <div className="max-w-7xl mx-auto sm:px-6 lg:px-8">
                    <div className="bg-white overflow-hidden shadow-sm sm:rounded-lg">
                        {list.data.map((model, i) => {
                            return <div> {model.id}</div>;
                        })}
                    </div>
                </div>
            </div>
        </AuthenticatedLayout>
    );
}
