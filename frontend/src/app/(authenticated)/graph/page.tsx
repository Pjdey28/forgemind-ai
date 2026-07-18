"use client";

import React, { useState, useEffect } from "react";
import { Network, HelpCircle, Activity } from "lucide-react";
import CyberCard from "@/components/ui/CyberCard";
import { getGraph } from "@/services/apiServices";

export default function KnowledgeGraphPage() {
  const [hoveredNode, setHoveredNode] = useState<string | null>(null);
  const [nodes, setNodes] = useState<any[]>([]);
  const [edges, setEdges] = useState<any[]>([]);

  useEffect(() => {
    const fetchGraphData = async () => {
      try {
        const res = await getGraph();
        if (res && res.data && res.data.nodes && res.data.nodes.length > 0) {
          const apiNodes = res.data.nodes;
          const apiEdges = res.data.edges;

          // Circular Layout positioning
          const centerX = 250;
          const centerY = 160;
          const radius = 95;

          const mappedNodes = apiNodes.map((n: any, idx: number) => {
            const angle = (idx / apiNodes.length) * 2 * Math.PI;
            return {
              id: n.id,
              label: n.id,
              x: centerX + radius * Math.cos(angle),
              y: centerY + radius * Math.sin(angle),
              desc: `Extracted Relational Entity. Type: [${n.label}]. Properties: ${
                Object.entries(n.properties)
                  .filter(([k]) => k !== "doc_id")
                  .map(([k, v]) => `${k}=${v}`)
                  .join(", ") || "None"
              }`
            };
          });

          const mappedEdges = apiEdges.map((e: any) => ({
            source: e.source,
            target: e.target
          })).filter((e: any) =>
            mappedNodes.some((n: any) => n.id === e.source) &&
            mappedNodes.some((n: any) => n.id === e.target)
          );

          setNodes(mappedNodes);
          setEdges(mappedEdges);
        } else {
          // Fall back to default demo graph if database is empty
          setNodes([
            { id: "cad", label: "Plant CAD Specs", x: 100, y: 70, desc: "Vectorized CAD drawings and structural engineering blueprints" },
            { id: "pdf", label: "Operations Manuals", x: 250, y: 50, desc: "1,204 Indexed manuals (compressor, generator, exchanger specs)" },
            { id: "neo4j", label: "Neo4j Graph Hub", x: 400, y: 70, desc: "82,000 Linked relations mapping operational documents to physical sensors" },
            { id: "scada", label: "SCADA Core Logs", x: 100, y: 220, desc: "Real-time logs stream mapping dynamic telemetry from sensor arrays" },
            { id: "astm", label: "ASTM Regulatory Rules", x: 250, y: 245, desc: "National factory regulations & OISD compliance validation checks" },
            { id: "rag", label: "Vector RAG Embeddings", x: 400, y: 220, desc: "ChromaDB database schema vector lookup and Llama 3 query synthesis loop" },
          ]);
          setEdges([
            { source: "cad", target: "pdf" },
            { source: "cad", target: "scada" },
            { source: "pdf", target: "neo4j" },
            { source: "pdf", target: "rag" },
            { source: "neo4j", target: "rag" },
            { source: "scada", target: "astm" },
            { source: "astm", target: "rag" },
          ]);
        }
      } catch (error) {
        console.error("Failed to load graph network", error);
      }
    };
    fetchGraphData();
  }, []);

  return (
    <div className="flex flex-col gap-6 select-none font-mono">
      
      <CyberCard 
        title="Neo4j Knowledge Network Explorer" 
        subtitle="Visualizing 82,000 active neural connections mapping plant documentation, regulations, and sensors"
        headerAction={
          <div className="flex items-center gap-1.5 bg-[#11141c] px-3 py-1.5 rounded border border-brand-primary/10">
            <Activity className="h-3.5 w-3.5 text-brand-success animate-pulse" />
            <span className="text-[10px] text-brand-success font-bold">GRAPH_SERVER_ONLINE</span>
          </div>
        }
      >
        <div className="w-full relative border border-brand-primary/10 rounded-xl bg-[#09090b]/80 overflow-hidden flex flex-col justify-between min-h-[500px]">
          
          {/* Top Help Tip banner */}
          <div className="p-3 border-b border-brand-primary/5 flex items-center gap-2 bg-[#11141c]/40 text-left">
            <HelpCircle className="h-4 w-4 text-brand-primary shrink-0" />
            <span className="text-[9px] text-brand-text-secondary leading-normal">
              INSTRUCTIONS: Hover over any network node to discover its connected operational context, document references, and adjacent sensor telemetry mappings.
            </span>
          </div>

          {/* Interactive SVG Network Layout Canvas */}
          <div className="flex-1 flex items-center justify-center p-6 relative min-h-[380px]">
            <svg className="w-full max-w-3xl h-[340px] text-brand-primary" viewBox="0 0 500 320">
              
              {/* Connection Edges */}
              {edges.map((edge, idx) => {
                const srcNode = nodes.find(n => n.id === edge.source)!;
                const tgtNode = nodes.find(n => n.id === edge.target)!;
                const isHighlighted = hoveredNode === edge.source || hoveredNode === edge.target;
                
                return (
                  <line
                    key={idx}
                    x1={srcNode.x}
                    y1={srcNode.y}
                    x2={tgtNode.x}
                    y2={tgtNode.y}
                    className={`stroke-current transition-all duration-300 ${
                      isHighlighted 
                        ? "stroke-2 text-brand-success opacity-90 filter drop-shadow-[0_0_5px_rgba(34,197,94,0.3)]" 
                        : "stroke-1 opacity-20 text-brand-primary"
                    }`}
                  />
                );
              })}

              {/* Graphic Nodes */}
              {nodes.map((node) => {
                const isHovered = hoveredNode === node.id;
                
                return (
                  <g
                    key={node.id}
                    className="cursor-pointer select-none"
                    onMouseEnter={() => setHoveredNode(node.id)}
                    onMouseLeave={() => setHoveredNode(null)}
                  >
                    <circle
                      cx={node.x}
                      cy={node.y}
                      r={isHovered ? 10 : 7}
                      className={`fill-[#0d0f14] stroke-current transition-all duration-300 ${
                        isHovered 
                          ? "stroke-brand-success stroke-2 filter drop-shadow-[0_0_12px_#22C55E]" 
                          : "stroke-brand-primary stroke-[1.5]"
                      }`}
                    />
                    <text
                      x={node.x}
                      y={node.y - 14}
                      textAnchor="middle"
                      className={`font-mono text-[9px] tracking-wide transition-colors duration-300 ${
                        isHovered ? "fill-brand-success font-bold" : "fill-brand-text-secondary"
                      }`}
                    >
                      {node.label}
                    </text>
                  </g>
                );
              })}
            </svg>
          </div>

          {/* Floating properties summary board */}
          <div className="p-4 border-t border-brand-primary/10 bg-[#0d0f14]/80 text-left">
            <div className="flex flex-col gap-1 min-h-[46px]">
              {hoveredNode ? (
                <>
                  <div className="text-[10px] text-brand-text-secondary">
                    NODE_ID: <span className="text-brand-success font-bold uppercase tracking-wider">{hoveredNode}</span>
                    <span className="mx-2 text-brand-primary/20">|</span>
                    MAPPING: <span className="text-brand-text-primary">82k relations active</span>
                  </div>
                  <div className="text-xs text-brand-text-primary font-semibold mt-0.5">
                    {nodes.find(n => n.id === hoveredNode)?.desc}
                  </div>
                </>
              ) : (
                <div className="text-center py-2 text-brand-text-secondary/40 text-[10px] flex items-center justify-center gap-1.5">
                  <Network className="h-4.5 w-4.5 text-brand-primary/30" />
                  Awaiting node inspect handshake. Hover mouse over knowledge graph endpoints to pull parameters metadata.
                </div>
              )}
            </div>
          </div>

        </div>
      </CyberCard>

    </div>
  );
}
