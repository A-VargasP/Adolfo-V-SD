import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Mail, ExternalLink, Code, X } from 'lucide-react';
import './index.css';
import './App.css';

function App() {
  const [projects, setProjects] = useState([]);
  const [categories, setCategories] = useState([]);
  const [activeCategory, setActiveCategory] = useState('All');
  const [selectedProject, setSelectedProject] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/projects')
      .then(res => setProjects(res.data))
      .catch(err => console.error("Error fetching projects", err));

    axios.get('http://127.0.0.1:5000/api/projects/categories')
      .then(res => setCategories(['All', ...res.data]))
      .catch(err => console.error("Error fetching categories", err));
  }, []);

  const filteredProjects = activeCategory === 'All' 
    ? projects 
    : projects.filter(p => p.category === activeCategory);

  return (
    <div className="container">
      {/* Header / Intro Section */}
      <header className="hero-section fade-in-down">
        <h1 className="hero-title">
          Hi, I'm <span className="gradient-text">Adolfo Nicolas Vargas</span>
        </h1>
        <h2 className="hero-subtitle">Management Information Systems Student</h2>
        <p className="hero-description">
          Welcome to my digital space. I am passionate about building innovative solutions and intuitive digital experiences.
        </p>
        <div className="social-links delay-1 fade-in-up">
          <a href="mailto:vargaspnicolas5@gmail.com" className="btn"><Mail size={18}/> Contact Me</a>
          <a href="https://github.com/A-VargasP" target="_blank" rel="noopener noreferrer" className="btn btn-outline"><ExternalLink size={18}/> GitHub</a>
          <a href="#" className="btn btn-outline"><ExternalLink size={18}/> LinkedIn</a>
        </div>
      </header>

      {/* About Section */}
      <section className="about-section delay-2 fade-in-up">
        <h3 className="section-title">About Me</h3>
        <div className="glass-panel">
          <p>
            I am a Management Information Systems student currently studying at Keiser University LAC. 
            With a focus on aligning technology with business strategy, I enjoy transforming complex problems 
            into elegant, reliable, and scalable web applications. Explore my portfolio below to see my 
            latest projects!
          </p>
          <p style={{ marginTop: '1rem' }}>
            <strong>Phone:</strong> +505 57011080 <br/>
            <strong>Email:</strong> vargaspnicolas5@gmail.com
          </p>
        </div>
      </section>

      {/* Projects Section */}
      <section className="projects-section delay-3 fade-in-up">
        <h3 className="section-title">Portfolio</h3>
        
        {/* Category Filter */}
        <div className="filter-container">
          {categories.map(cat => (
            <button 
              key={cat} 
              className={`filter-btn ${activeCategory === cat ? 'active' : ''}`}
              onClick={() => setActiveCategory(cat)}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Project Grid */}
        <div className="project-grid">
          {filteredProjects.map(project => (
            <div key={project.id} className="glass-panel project-card" onClick={() => setSelectedProject(project)} style={{cursor: 'pointer'}}>
              {project.is_sample === 1 ? <span className="sample-badge">Sample</span> : null}
              <div className="project-header">
                <Code className="project-icon" />
                <h4>{project.title}</h4>
              </div>
              <p className="project-desc">{project.description}</p>
              <div className="project-footer">
                <span className="project-category">{project.category}</span>
                {project.link && (
                  <a href={project.link} target="_blank" rel="noopener noreferrer" className="project-link" onClick={(e) => e.stopPropagation()}>
                    View <ExternalLink size={14} />
                  </a>
                )}
              </div>
            </div>
          ))}
        </div>
      </section>
      {/* Project Modal Overlay */}
      {selectedProject && (
        <div className="modal-overlay" onClick={() => setSelectedProject(null)}>
          <div className="modal-content glass-panel" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={() => setSelectedProject(null)}>
              <X size={24} />
            </button>
            <div className="project-header" style={{ marginBottom: '1.5rem' }}>
              <Code className="project-icon" size={32} />
              <h2 style={{ fontSize: '2rem' }}>{selectedProject.title}</h2>
            </div>
            <span className="project-category" style={{ display: 'inline-block', marginBottom: '1.5rem', background: 'rgba(255, 255, 255, 0.1)', padding: '0.25rem 0.75rem', borderRadius: '6px' }}>{selectedProject.category}</span>
            <p className="project-desc" style={{ fontSize: '1.1rem', marginBottom: '2rem', color: 'var(--text-secondary)' }}>
              {selectedProject.description}
            </p>
            {selectedProject.link && (
              <a href={selectedProject.link} target="_blank" rel="noopener noreferrer" className="btn">
                <ExternalLink size={18}/> View Project
              </a>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
