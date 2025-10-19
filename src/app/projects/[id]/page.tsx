import { projects } from '../../../../data/projects';
import { notFound } from 'next/navigation';

// This function tells Next.js which project IDs are valid
// and should be turned into pages at build time.
export function generateStaticParams() {
  return projects.map((project) => ({
    id: project.id.toString(),
  }));
}

// The page component receives the 'id' from the URL as a prop.
export default function ProjectDetailPage({ params }: { params: { id: string } }) {
  // Find the specific project based on the ID from the URL.
  const project = projects.find(p => p.id.toString() === params.id);

  // If no project is found for the given ID, show a 404 page.
  if (!project) {
    notFound();
  }

  return (
    <main className="container mx-auto p-8">
      <h1 className="text-5xl font-extrabold mb-4">{project.title}</h1>
      <p className="text-lg text-gray-700 mb-6">{project.description}</p>

      <div className="flex flex-wrap gap-2">
        <h3 className="text-xl font-semibold w-full mb-2">Technologies Used:</h3>
        {project.technologies.map((tech) => (
          <span key={tech} className="bg-blue-100 text-blue-800 text-md font-medium px-3 py-1 rounded-full">
            {tech}
          </span>
        ))}
      </div>
    </main>
  );
}