import {projects} from "../../../data/projects";
import Link from "next/link";

export default function ProjectsPage() {
  return (
    <main className="container mx-auto p-8">
      <h1 className="text-4xl font-bold mb-4">My Projects</h1>
      {/* We will add project cards here soon */}
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
  {projects.map((project) => (
    <Link key={project.id} href={`/projects/${project.id}`} className="block">
      <div className="border border-gray-200 rounded-lg p-6 shadow-md hover:shadow-xl transition-shadow bg-white h-full">
        <h2 className="text-2xl font-bold mb-2 text-amber-600">{project.title}</h2>
        <p className="text-gray-700 mb-4">{project.description}</p>
        <div className="flex flex-wrap gap-2">
          {project.technologies.map((tech) => (
            <span key={tech} className="bg-gray-200 text-gray-800 text-sm font-medium px-2.5 py-0.5 rounded">
              {tech}
            </span>
          ))}
        </div>
      </div>
    </Link>
  ))}
</div>
    </main>
  );
}