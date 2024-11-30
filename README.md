# Metro Router CDMX

A sophisticated route planning system for Mexico City's Metro network, implementing a hybrid reasoning approach combining Case-Based Reasoning (CBR) and Model-Based Reasoning, inspired by the Router system described in CogSci 1993.

## Overview

Metro Router Final 2 is an intelligent transportation routing system that helps users find optimal routes between stations in Mexico City's Metro network. The system implements a hybrid reasoning approach that combines:

- Case-Based Reasoning (CBR) to leverage successful past routes
- Model-Based Reasoning with hierarchical maps for systematic route planning
- Zone-based hierarchical organization of the metro network
- Recursive descent path finding algorithm

### Key Features

- Hybrid reasoning system combining multiple approaches
- Hierarchical organization of the metro network into zones and sub-zones
- Pre-loaded base cases for common routes
- Detailed route information including transfers and estimated times
- Comprehensive logging of the reasoning process
- Statistical analysis of system usage

## System Architecture

### Core Components

1. **MetroRouterHibrido**: Main class implementing the hybrid reasoning approach
   - Combines case-based and model-based reasoning
   - Manages the decision-making process between different reasoning methods
   - Handles route finding and optimization

2. **GestorCasos**: Case management system
   - Manages the case base using a decision tree structure
   - Handles case storage and retrieval
   - Implements case similarity assessment
   - Manages base cases and learned routes

3. **GestorRutas**: Model-based reasoning implementation
   - Implements recursive descent algorithm
   - Manages hierarchical map structure
   - Handles zone-based route planning
   - Manages transitions between zones

### Data Structures

- `Station`: Represents metro stations with their properties
- `Caso`: Represents stored route cases with usage statistics
- `metro_cdmx`: Dictionary containing the complete metro network
- `zonas`: Hierarchical organization of the network into zones and sub-zones

## Usage

### Basic Operation

```python
# Initialize the router
router = MetroRouterHibrido(metro_cdmx, zonas, verbose=True)

# Find a route
ruta, metodo = router.encontrar_ruta(origen, destino)
```

### Command-line Interface

The system provides a command-line interface with the following options:

1. Search for a route
2. View stations by line
3. View system statistics
4. Exit

### Route Information

For each route, the system provides:
- Complete station sequence
- Required transfers
- Total number of stations
- Estimated travel time
- Reasoning method used (case-based or model-based)

## Implementation Details

### Reasoning Process

1. **Initial Analysis**
   - Identifies zones and sub-zones for origin and destination
   - Evaluates available cases

2. **Case-Based Reasoning**
   - Searches for similar previous routes
   - Evaluates case quality and usage statistics
   - Adapts previous solutions if needed

3. **Model-Based Reasoning**
   - Uses hierarchical map structure
   - Implements recursive descent algorithm
   - Handles zone transitions
   - Plans inter-zonal routes

4. **Route Selection**
   - Evaluates routes from both methods
   - Selects optimal solution
   - Stores new routes as cases

### Performance Considerations

- Case-based reasoning prioritizes routes with high usage and good ratings
- Model-based reasoning provides systematic coverage of the network
- Hybrid approach ensures both efficiency and reliability
- Hierarchical organization reduces search space

## System Requirements

- Python 3.7 or higher
- No external dependencies required
- Sufficient memory to store case base and network structure

## Limitations and Future Work

- Limited to Mexico City's Metro network
- Does not account for real-time conditions
- Could be extended to include:
  - Real-time updates
  - Multi-modal transportation
  - Dynamic route optimization
  - User preferences
  - Alternative route suggestions

## Contributing

Contributions are welcome! Please consider:

- Adding new base cases
- Improving route optimization
- Extending the network coverage
- Enhancing the user interface
- Adding new features

## License

This project is licensed under the MIT License - see the LICENSE file for details.
